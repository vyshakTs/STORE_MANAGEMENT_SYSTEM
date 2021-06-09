from django.shortcuts import render
from django.views import generic

from .models import Category, Product, SubCategory


# Create your views here.
class ProductListView(generic.ListView):
    model = Product
    template_name = 'products/index.html'
    context_object_name = 'products'

class ProductDetailView(generic.DetailView):
    pass