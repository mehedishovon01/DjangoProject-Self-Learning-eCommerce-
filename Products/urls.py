from django.urls import path
# from . import views
from .views import (
    GetProductListView,
    # GetProductDetailsView,
    GetProductDetailsSlugView
)


urlpatterns = [
    path('product-list', GetProductListView.as_view(), name='product_list'),
    # path('<str:name>/details/<int:pk>', GetProductDetailsView.as_view(), name='product-details'),
    path('<str:name>/details/<str:slug>', GetProductDetailsSlugView.as_view(), name='product-details'),
]
