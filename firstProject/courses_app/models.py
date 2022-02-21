from django.db import models


class Course(models.Model) :

    title = models.CharField(max_length=30)
    teacher_fullname = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return self.title

