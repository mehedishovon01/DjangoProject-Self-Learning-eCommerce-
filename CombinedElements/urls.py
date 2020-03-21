from django.urls import path
from .views import (
    CategoryWiseProductListView,
)


urlpatterns = [
    path('<str:name>/', CategoryWiseProductListView.as_view(), name='category-wise-products'),
]
