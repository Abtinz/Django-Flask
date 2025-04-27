from django.shortcuts import render
from django.http import HttpResponse
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


def say_hello_html(request):
    return render(request,'hello.html', {'response': 'Hello again old friend!'})
