from django.shortcuts import render
from .models import user_information
def home(request):
    return render(request , "BlogApp/home.html")

def contact(request):
    return render(request,"BlogApp/contact.html")

def account(request , username):
    user = user_information.objects.get(username = username)
    return render(request,"BlogApp/account.html" , context={"account" : user})
