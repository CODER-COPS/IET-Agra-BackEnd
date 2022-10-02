from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Carousel(models.Model):
    added_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, default='')
    photo = models.ImageField(upload_to='carousal')
    is_active = models.BooleanField(default=False)
    preference = models.IntegerField(unique=True,
                                     validators=[MaxValueValidator(6), MinValueValidator(1)])

    class Meta:
        ordering = ['added_at']

    def __str__(self):
        return self.title
