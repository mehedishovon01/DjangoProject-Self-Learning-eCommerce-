from django.shortcuts import render
from CombinedElements.models import Category


def home(request):
    context = {
        'category_name': Category.objects.all()
    }
    return render(request, 'home/home.html', context)


def contact_us(request):
    return render(request, 'home/contact-us.html')


def about(request):
    return render(request, 'home/about.html')
