from django.db import models

class user_information(models.Model):

    full_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    Bio = models.TextField()

    def __str__(self):
        return self.username

