from django.contrib import admin
from django.urls import include, path

from . import views
from .views import ProductDetailView, ProductListView

urlpatterns = [
    path('', ProductListView.as_view(), name='products'),
    path('details/<int:pk>', ProductDetailView.as_view(), name='product_details'),
]