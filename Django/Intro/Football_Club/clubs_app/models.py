from email.policy import default
from django.db import models

class Clube(models.Model):
     name = models.CharField(max_length = 30)
     foundation_date = models.DateField()
     trophies_count = models.IntegerField(default=0)
     league_title = models.CharField(max_length = 30)
     country = models.CharField(max_length = 30)
     rank = models.IntegerField()
     situation =  models.CharField(max_length = 30 ,default="OnFire")
     club_logo = models.ImageField(default = "img\default.png")
     def __str__(self):
          return self.name
