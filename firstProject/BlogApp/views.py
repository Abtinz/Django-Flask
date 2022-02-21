from django.shortcuts import render,HttpResponse

def home(request):
    return render(request , "BlogApp/home.html")

def contact(request):
    return render(request,"BlogApp/contact.html")

def account(request , username):
    return render(request,"BlogApp/account.html" , context={"username" : username})
