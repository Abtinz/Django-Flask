from django.shortcuts import render , HttpResponse

def home(request):
    return HttpResponse('welcom to football club app')
