from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(default='', upload_to='category')
    posted_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50)
    posted_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Color(models.Model):

    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
