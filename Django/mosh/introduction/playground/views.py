from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from store.models import Product
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

def say_hello_html(request):
    return render(request,'hello.html', {'response': 'Hello again old friend!'})
