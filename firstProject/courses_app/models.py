from sys import modules
from django.db import models


class Course(models.Model) :

    title = models.CharField(max_length=30)
    teacher_fullname = models.CharField(max_length=30)
    description = models.TextField()
    status = models.BooleanField(default=True)
    attenders = models.IntegerField(default=0)
    sessions = models.IntegerField(default=0)
    #started_date  = models.TimeField()

    def __str__(self):
        return self.title

