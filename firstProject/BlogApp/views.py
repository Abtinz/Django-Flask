from django.shortcuts import render
from .models import user_information
def home(request):
    return render(request , "BlogApp/home.html")

def contact(request):
    return render(request,"BlogApp/contact.html")

def new_account(request):
    full_name = request.GET.get("full_name")
    username = request.GET.get("username")
    password = request.GET.get("password")
    email = request.GET.get("email")
    Bio = request.GET.get("Bio")
    if full_name and username :
        if password and email and Bio:
            user_information.objects.create(full_name = full_name ,
                                              username = username , 
                                              password = password ,
                                              email = email ,
                                              Bio = Bio
                                              )
            user = user_information.objects.get(username = username)
            return render(request,"BlogApp/account.html" , context={"account" : user})
    return render(request,"BlogApp/new_account.html")

def account(request , username):
    user = user_information.objects.get(username = username)
    return render(request,"BlogApp/account.html" , context={"account" : user})
