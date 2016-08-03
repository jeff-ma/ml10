from django.db import models
from django.utils import timezone

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    authors = models.CharField(max_length=200)
    publish_date = models.DateField(default=timezone.now)
    publisher = models.CharField(max_length=150)
    summary = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    link = models.URLField()
    image = models.URLField()

    class Meta:
        ordering = ('title',)
