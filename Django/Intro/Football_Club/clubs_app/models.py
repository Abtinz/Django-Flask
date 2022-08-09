from django.db import models

class Clube(models.Model):
     name = models.CharField(max_length = 30)
     foundation_date = models.DateField()
     trophies_count = models.IntegerField(default=0)
     league_title = models.CharField(max_length = 30)
     country = models.CharField(max_length = 30)