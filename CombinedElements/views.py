from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from Products.models import Product
from CombinedElements.models import Category


class CategoryWiseProductListView(ListView):
    model = Product
    template_name = 'category/category-wise-list.html'
    context_object_name = 'category_wise_product_view'
    ordering = ['-posted_date']
    paginate_by = 10

    def get_queryset(self):
        self.category = get_object_or_404(Category, name=self.kwargs['name'])
        return Product.objects.filter(category=self.category).order_by('-posted_date')

        # def get_context_data(self, *, object_list=None, **kwargs):
        #     context = super(ShirtListView, self).get_context_data(**kwargs)
        #     context['categories'] = self.category
        #     return context

    # Add Another Model For Passing Data
    def get_context_data(self, **kwargs):
        context = super(CategoryWiseProductListView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
