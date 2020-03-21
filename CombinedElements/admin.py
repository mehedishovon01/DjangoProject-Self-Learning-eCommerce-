from django.contrib import admin
from .models import (
    Category,
    SubCategory,
    Color
)

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Color)
