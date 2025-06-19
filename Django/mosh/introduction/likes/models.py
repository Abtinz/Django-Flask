from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class LikedItem(models.Model):
    #Here with settings.AUTH_USER_MODEL we can maintain our dependency from store app in new user definition
    user = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete= models.CASCADE)
    #Generic content type, id, object
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveSmallIntegerField()
    content_object = GenericForeignKey()