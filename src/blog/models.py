from django.conf import settings
from django.db import models
# Create your models here.

User = settings.AUTH_USER_MODEL

class BlogPost(models.Model):
    user    = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    content  = models.IntegerField(null=True, blank=False)
