from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Hello Django </br>Abtin Zandi : 19 : Theran </br>This is Home page for path test in django!")

def contact(request):
    return HttpResponse("Contact us : </br>GitHub : Abtinz </br> Email : NotAbtin@FakeEmail.com" )

def account(request , username):
    return HttpResponse(f"Account:</br>UserName:{username}</br>Hi {username}</br>this is your django profile" )