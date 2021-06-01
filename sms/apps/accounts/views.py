# Create your views here.
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic

from sms.apps.customers.models import CustomerProfile

from .forms import CustomAuthentication, UserCreationForm
from .models import User


class CustomerProfileView(generic.TemplateView):
    model = CustomerProfile
    template_name = 'accounts/index.html'


class StoreRegistrationView(generic.FormView):
    form_class = UserCreationForm
    template_name = 'account/store_registration.html'
    success_url = reverse_lazy('store_profile')
    redirect_url = 'store_dashboard'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(self.redirect_url)
        return super().get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['button_value'] = 'Create store'
        context['page_headline'] = 'Create your store'
        return context
    
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['initial'] = {
            'user_type': User.STORE_OWNER
        }
        return kwargs

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user,
                  backend=settings.AUTHENTICATION_BACKENDS[0])
        return super().form_valid(form)
    
    
class CustomerRegistrationView(StoreRegistrationView):
    success_url = reverse_lazy('home')
    redirect_url = reverse_lazy('home')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['button_value'] = 'Create Account'
        context['page_headline'] = 'Create your Account'
        return context
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['initial'] = {
            'user_type': User.CUSTOMER,
        }
        return kwargs
    

class EmployeeRegistrationView(CustomerRegistrationView):
    success_url = reverse_lazy('home')
    redirect_url = reverse_lazy('home')
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['initial'] = {
            'user_type': User.EMPLOYEE,
        }
        return kwargs
        

class UserLoginView(generic.FormView):
    form_class = CustomAuthentication
    template_name = 'account/store_login.html'
    redirect_authenticated_user = True
    redirect_field_name = 'next'
    
    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('store_dashboard')
        return super().get(request, *args, **kwargs)
    
    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user.is_active:
            login(self.request, user, backend=settings.AUTHENTICATION_BACKENDS[0])
            if user.is_SO:
                reverse_url = 'store_dashboard'
            elif user.is_EMPLOYEE:
                reverse_url = 'home'
            elif user.is_CUSTOMER:
                reverse_url = 'home'
        return redirect(reverse_url)
        