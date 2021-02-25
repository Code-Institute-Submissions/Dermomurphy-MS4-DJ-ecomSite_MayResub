from django.db import models
from datetime import datetime
# Create your models here.

class Posts(models.Model):
    class Meta:
     
        verbose_name_plural = 'Posts'

    title = models.CharField(max_length=254)
    body = models.TextField()
    image = models.ImageField(default='noimage.png')
    created_on = models.DateTimeField(default=datetime.now, blank=True)
