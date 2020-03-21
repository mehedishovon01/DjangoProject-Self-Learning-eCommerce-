from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
# from CombinedElements.models import Category
from .models import Product
from CombinedElements.models import Category
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)


class GetProductListView(ListView):
    model = Product
    template_name = 'products/product-list.html'
    context_object_name = 'products'
    ordering = ['-posted_date']
    paginate_by = 10

    # Add Another Model For Passing Data
    # def get_context_data(self, **kwargs):
    #     context = super(GetProductListView, self).get_context_data(**kwargs)
    #     context['categories'] = Category.objects.all()
    #     return context

    # Add Another Model For Passing Data
    def get_context_data(self, **kwargs):
        context = super(GetProductListView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class GetProductDetailsView(DetailView):
    model = Product
    template_name = 'products/product-details.html'
