from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('profile/', views.StoreProfileCreationView.as_view(), name='store_profile'),
    path('dashboard/', views.StoreProfileView.as_view(), name='store_dashboard'),
]
