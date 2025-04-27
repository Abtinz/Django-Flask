from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from store.models import Product
from decimal import Decimal, InvalidOperation
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
    ).order_by("unit_price")          

    products = list(products_qs.values("id", "title", "unit_price", "inventory"))

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


def say_hello_html(request):
    return render(request,'hello.html', {'response': 'Hello again old friend!'})
