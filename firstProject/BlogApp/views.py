from django.shortcuts import render,HttpResponse

# Create your views here.
def firstPage(request):
    return HttpResponse("Hello Django\nAbtin Zandi : 19 : Theran")