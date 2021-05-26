from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('home/', views.CustomerProfileView.as_view(), name='home'),
    # path('profile/<str:slug>', views.UserProfileView.as_view(), name='profile'),
    path('signup/', views.StoreRegistrationView.as_view(), name='user_signup'),
    path('login/', views.UserLoginView.as_view(), name='user_login'),
    # path('profile/edit/<str:slug>', views.UserProfileUpdateView.as_view(), name='edit_profile'),
]
