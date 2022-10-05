from django.db import models
from ckeditor.fields import RichTextField


class Notification(models.Model):
    added_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, default='')
    description = RichTextField()
    is_active = models.BooleanField(default=False)

    class Meta:
        ordering = ['added_at']

    def __str__(self):
        return self.title
