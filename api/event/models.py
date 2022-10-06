from django.db import models

# Create your models here.

class Event(models.Model):
    added_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, default = '')
    is_active = models.BooleanField(default = False)
