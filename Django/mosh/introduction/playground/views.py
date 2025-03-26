from django.shortcuts import render
from django.http import HttpResponse
import json
# Create your views here.

def say_hello(request):

    response_data = {
        "response": "Hello again old friend!",
        "status_code": "200"
    }

    return HttpResponse(
        content= json.dumps(response_data), 
        content_type="application/json"
    )

def say_hello_html(request):
    return render(request,'hello.html', {'response': 'Hello again old friend!'})
