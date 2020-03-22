from django.db import models
from django.utils import timezone
from CombinedElements.models import (
    Category,
    SubCategory,
    Color,
)


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    size = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    # subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    short_description = models.TextField()
    full_description = models.TextField()
    manufacturer = models.TextField()
    picture = models.ImageField(default='products/default.jpg', upload_to='products')
    posted_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Image(models.Model):
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    image1 = models.ImageField(default='products/default.jpg', upload_to='products', null=True, blank=True)
    image2 = models.ImageField(default='products/default.jpg', upload_to='products', null=True, blank=True)

    def __str__(self):
        return self.product_name.name
