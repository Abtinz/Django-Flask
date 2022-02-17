from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return render(request , "BlogApp/home.html")

def contact(request):
    return render(request,"BlogApp/contact.html")

def account(request , username):
    return render(request,"BlogApp/account.html")
    #return HttpResponse(f"Account:</br>UserName:{username}</br>Hi {username}</br>this is your django profile" )