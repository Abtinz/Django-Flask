from django.shortcuts import render
from .models import Course

def courses_list(request):
    courses = Course.objects.all()
    return render(request , "courses_app/courses_lists.html" , context={ "courses" : courses})

def course_information(request , course_id):
     course = Course.objects.get(id = course_id)
     
     return render(request , "courses_app/course_information.html" , context={ "course" : course})