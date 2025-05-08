from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from store.models import Order, Product, OrderItem, Collection
from tags.models import TagItem
from django.db.models import F, Value, IntegerField #annotation
from django.db.models import Q 
from django.db.models import Min, Max, Avg, Count #aggregation
from django.db import transaction #transactions -> atomic
from decimal import Decimal, InvalidOperation
from django.contrib.contenttypes.models import ContentType
import json

def say_hello(request):

    response_data = {
        "response": "Hello again old friend!",
        "status_code": "200"
    }

    return HttpResponse(
        content= json.dumps(response_data), 
        content_type="application/json"
    )

def all_products(request):

    query_set = Product.objects.all()

    products = []
    for product in query_set:
        products.append(product)
        print(product)

    response_data = {
        "response": "products list!",
        "products": f"{products}",
        "status_code": "200"
    }

    return HttpResponse(
        content= json.dumps(response_data), 
        content_type="application/json"
    )

def ordered_products(request):

    query_set = OrderItem.objects.order_by("-product__title").distinct().values("product__title","product__unit_price","product__inventory","product__collection")

    products = list(query_set)

    if not products:
        return JsonResponse(
            {
                "error": (
                    f"No products have been ordered yet!"
                )
            },
            status=404
        )

    return JsonResponse(
        {
            "count": len(products),
            "products": products,
            "status_code": 200
        }
    )

def products_by_id(request):
    """
    Return the product whose primary-key is supplied through the `id`
    query parameter, e.g.  GET /products/?id=5
    """

    product_id = request.GET.get("id")
    if not product_id:
        return JsonResponse(
            {"error": "`id` query parameter is required"}, status=400
        )

    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return JsonResponse(
            {"error": f"Product with id {product_id} not found"}, status=404
        )

    return JsonResponse(
        {
            "response": f"product id – {product_id}",
            "product": str(product), 
            "status_code": 200,
        }
    )

def expensive_products(request):
    """
    GET /products/?price_threshold=20
    Returns every product whose unit_price exceeds the value supplied in
    the `price_threshold` query-string parameter.
    """

    raw_threshold = request.GET.get("price_threshold")
    if raw_threshold is None:
        return JsonResponse({"error": "`price_threshold` is required"}, status=400)

    try:
        threshold = Decimal(raw_threshold)
    except InvalidOperation:
        return JsonResponse(
            {"error": "`price_threshold` must be a numeric value"}, status=400
        )

    products_qs = Product.objects.filter(unit_price__gt=threshold)

    products = list(
        products_qs.values("id", "title", "unit_price")
    ) 

    if not products:
        return JsonResponse(
            {"error": f"No products cost more than {threshold}"}, status=404
        )

    return JsonResponse(
        {
            "price_threshold": str(threshold),
            "count": len(products),
            "products": products,
            "status_code": 200,
        }
    )

def range_of_prices(request):
    """
    GET /products/range/?min_price=40&max_price=50
    Returns every product whose unit_price lies within the inclusive
    [min_price, max_price] range supplied in the query-string.
    """

    raw_min = request.GET.get("min_price")
    raw_max = request.GET.get("max_price")

    if raw_min is None or raw_max is None:
        return JsonResponse(
            {"error": "`min_price` and `max_price` query parameters are required"},
            status=400,
        )

    try:
        min_price = Decimal(raw_min)
        max_price = Decimal(raw_max)
    except InvalidOperation:
        return JsonResponse(
            {"error": "Both `min_price` and `max_price` must be numeric values"},
            status=400,
        )

    if min_price > max_price:
        return JsonResponse(
            {"error": "`min_price` cannot be greater than `max_price`"}, status=400
        )

    products_qs = Product.objects.filter(
        unit_price__range = (min_price,max_price)
    ).order_by("unit_price")   

    products = list(products_qs.values("id", "title", "unit_price"))

    if not products:
        return JsonResponse({"error": f"No products found in the {min_price}–{max_price} price range"},status=404)

    return JsonResponse(
        {
            "min_price": str(min_price),
            "max_price": str(max_price),
            "count": len(products),
            "products": products,
            "status_code": 200
        }
    )

def expensive_low_stock(request):
    """
    GET /products/check/?min_price=50&max_inventory=10
    Returns every product whose:
        • unit_price  >  min_price
        • inventory   <  max_inventory
    """

    raw_price = request.GET.get("min_price")
    raw_stock = request.GET.get("max_inventory")

    if raw_price is None or raw_stock is None:
        return JsonResponse(
            {"error": "min_price and max_inventory are required"}, status=400
        )

    try:
        min_price = Decimal(raw_price)
        max_inventory = int(raw_stock)
    except (InvalidOperation, ValueError):
        return JsonResponse(
            {"error": "Both query parameters must be numeric"}, status=400
        )

    #complex query with filters
    products_qs = Product.objects.filter(
        unit_price__gt=min_price,
        inventory__lt=max_inventory,
    ).order_by("unit_price").values("id", "title", "unit_price", "inventory", "collection__title")    

    products = list(products_qs)

    if not products:
        return JsonResponse(
            {
                "error": (
                    f"No products cost more than {min_price} and have inventory "
                    f"under {max_inventory}"
                )
            },
            status=404,
        )

    return JsonResponse(
        {
            "min_price": str(min_price),
            "max_inventory": max_inventory,
            "count": len(products),
            "products": products,
            "status_code": 200,
        }
    )

def cheap_plenty_stock(request):
    """
    GET /products/check/cheap/plenty/?max_price=50&min_inventory=10
    Returns every product whose:
        • unit_price  <  min_price
        • inventory   >  max_inventory
    """

    raw_price = request.GET.get("max_price")
    raw_stock = request.GET.get("min_inventory")

    if raw_price is None or raw_stock is None:
        return JsonResponse(
            {"error": "max_price and min_inventory are required"}, status=400
        )

    try:
        max_price = Decimal(raw_price)
        min_inventory = int(raw_stock)
    except (InvalidOperation, ValueError):
        return JsonResponse(
            {"error": "Both query parameters must be numeric"}, status=400
        )
    
    #complex query with filters using Q
    products_qs = Product.objects.filter(
        Q(unit_price__lt=max_price) & Q(inventory__gt=min_inventory)
    ).order_by("unit_price")  

    products = list(products_qs.values("id", "title", "unit_price", "inventory"))

    if not products:
        return JsonResponse(
            {
                "error": (
                    f"No products cost less than {max_price} and have inventory "
                    f"more than {min_inventory}"
                )
            },
            status=404,
        )

    return JsonResponse(
        {
            "min_price": str(max_price),
            "max_inventory": min_inventory,
            "count": len(products),
            "products": products,
            "status_code": 200,
        }
    )

def unit_price_stats(request):
    """
    GET /products/statistics/
    Returns min, max, and average unit_price across *all* products.
    """
    statistics = Product.objects.aggregate(
        count = Count("id"),
        min_price=Min("unit_price"),
        max_price=Max("unit_price"),
        avg_price=Avg("unit_price"),
    )

    
    if all(value is None for value in statistics.values()):
        return JsonResponse(
            {"error": "No products has been added to database until now, we cannot show and compute required statistics"}, 
            status=404
        )

    # Convert Decimal / None to strings for JSON-safe output
    response_data = {
        "product counts": str(statistics["count"]) if statistics["count"] is not None else None,
        "min_price": str(statistics["min_price"]) if statistics["min_price"] is not None else None,
        "max_price": str(statistics["max_price"]) if statistics["max_price"] is not None else None,
        "avg_price": str(statistics["avg_price"]) if statistics["avg_price"] is not None else None,
        "status_code": 200,
    }

    return JsonResponse(response_data)

def collection_price_stats(request):
    """
    GET /products/collection-stats/?collection_title=<name>
    Filters products by `collection_title` (case-insensitive) and then returns
    min, max, and average unit_price for that subset.
    """

    collection_title = request.GET.get("collection_title")
    if collection_title is None:
        return JsonResponse(
            {"error": "bad request: collection_title query parameter is required"}, 
            status=400
        )

    qs = Product.objects.filter(collection__title__iexact=collection_title.strip())

    if not qs.exists():
        return JsonResponse(
            {"error": f"No products found in collection {collection_title}"},
            status=404
        )

    stats = qs.aggregate(
        count = Count("id"),
        min_price=Min("unit_price"),
        max_price=Max("unit_price"),
        avg_price=Avg("unit_price")
    )

    response_data = {
        "collection_title": collection_title,
        "count": str(stats["count"]),
        "min_price": str(stats["min_price"]),
        "max_price": str(stats["max_price"]),
        "avg_price": str(stats["avg_price"]),
        "product_count": qs.count(),
        "status_code": 200
    }

    return JsonResponse(response_data)

def products_union_id(request):
    """
    GET /products/union/id/
    Adds 10 080 to every product’s primary-key and returns both the original
    `id` and the computed `new_id`.  (10 080 = 7 days × 24 h × 60 min,
    if you are wondering about the offset.)
    """

    products_qs = (
        Product.objects.annotate(new_id=F("id") + Value(10080, output_field=IntegerField()))
        .values("new_id", "title","unit_price","collection")
        .order_by("new_id")
    )

    products = list(products_qs)

    if not products:
        return JsonResponse({"error": "No products in database"}, status=404)

    return JsonResponse(
        {
            "products": products,
            "status_code": 200
        }, status=200
    )

def new_collection(request):
    """
    GET /collection/add/
    this endpoint function will implement insert sql command using ORM for collections
    """

    collection_title = request.GET.get("collection_title")
    featured_product = request.GET.get("featured_product")

    if collection_title is None or featured_product is None:
        return JsonResponse(
            {"error": "bad request: collection_title and featured_product query parameter is required"}, 
            status=400
        )
    
    product = Product(pk=int(featured_product))
    
    query_set = Collection.objects.create(title = collection_title ,featured_product= product)

    if query_set is None:
        return JsonResponse({"error": "Server Error"}, status=500)

    return JsonResponse(
        {
            "new collection": str(query_set),
            "status_code": 200
        }, status=200
    )

def update_collection(request):
    """
    GET /collection/update/
    this endpoint function will implement insert sql command using ORM for collections
    """

    collection_id = request.GET.get("collection_id")
    collection_title = request.GET.get("collection_title")
    featured_product = request.GET.get("featured_product")

    if collection_title is None or featured_product is None or collection_id is None:
        return JsonResponse(
            {"error": "bad request: collection_id and collection_title and featured_product are query parameters and required"}, 
            status=400
        )
    

    product = Product(pk=int(featured_product)) if featured_product != "None" else None
    
    query_set = Collection.objects.filter(pk=int(collection_id)).update(title = collection_title ,featured_product= product)

    if query_set is None:
        return JsonResponse({"error": "Server Error"}, status=500)

    return JsonResponse(
        {
            "new collection": str(query_set),
            "status_code": 200
        }, status=200
    )

@transaction.atomic()
def new_order(request):
    
    with transaction.atomic():
        """
        GET /order/new/
        this endpoint function will implement insert sql command using ORM for orders in atomic way!
        """

        customer_id = request.GET.get("customer_id")
        product_id = request.GET.get("product_id")
        product_quantity = request.GET.get("product_quantity")


        if product_id is None or product_quantity is None or customer_id is None:
            return JsonResponse(
                {"error": "bad request: collection_id and product_id and featured_product are query parameters and required"}, 
                status=400
            )

        
        product_price = Product.objects.filter(pk=int(product_id)).values("unit_price")
        

        if product_price is None:
            return JsonResponse(
                {"error": "bad request: no product with this given id has found"}, 
                status=400
            )
        
        print(product_price[0]["unit_price"])
        order_price = int(product_price[0]["unit_price"]) * int(product_quantity)

        

        order = Order()
        order.customer_id = int(customer_id)
        order.save()

        orderItem = OrderItem()
        orderItem.order = order
        orderItem.product = Product(pk = int(product_id))
        orderItem.quantity = int(product_quantity)
        orderItem.unit_price = order_price
    
        orderItem.save()
        
        if orderItem is None:
            return JsonResponse({"error": "Server Error"}, status=500)

        return JsonResponse(
            {
                "new collection": str(orderItem),
                "status_code": 200
            }, status=200
        )

def tags_generic_content_type(request):

    content_type = ContentType.objects.get_for_model(Product)


    query_set = TagItem.objects \
        .select_related('tag') \
        .filter(
            content_type=content_type,
            object_id = 1
        )
    
    tags = list(query_set)
    
    return JsonResponse(
        {
            "count": len(tags),
            "tags": tags,
            "status_code": 200
        }
    )


    

def say_hello_html(request):
    return render(request,'hello.html', {'response': 'Hello again old friend!'})
