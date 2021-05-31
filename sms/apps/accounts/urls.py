from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('home/', views.CustomerProfileView.as_view(), name='home'),
    # path('profile/<str:slug>', views.UserProfileView.as_view(), name='profile'),
    path('store/signup/', views.StoreRegistrationView.as_view(), name='store_signup'),
    path('employee/signup/', views.EmployeeRegistrationView.as_view(), name='employee_signup'),
    path('customer/signup/', views.CustomerRegistrationView.as_view(), name='customer_signup'),
    path('login/', views.UserLoginView.as_view(), name='user_login'),
    # path('profile/edit/<str:slug>', views.UserProfileUpdateView.as_view(), name='edit_profile'),
]
