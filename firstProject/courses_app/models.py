from django.db import models


class Course(models.Model) :

    course_title = models.CharField(max_length=30)
    course_teacher_fullname = models.CharField(max_length=30)
    course_description = models.TextField()

def __str__(self):
    return 

