from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class Tag(models.Model):
    label = models.CharField(unique=True , max_length=255)

class TagItem(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    #Generic content type, id, object
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveSmallIntegerField()
    content_object = GenericForeignKey()