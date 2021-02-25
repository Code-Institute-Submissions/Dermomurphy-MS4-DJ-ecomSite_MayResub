from django.db import models
from datetime import datetime
# Create your models here.

class Posts(models.Model):
    title = models.CharField(max_length=254)
    body = models.TextField()
    created_on = models.DateTimeField(default=datetime.now, blank=True)
