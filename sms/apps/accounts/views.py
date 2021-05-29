# Create your views here.
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic

from apps.customers.models import CustomerProfile

from .forms import CustomAuthentication, UserCreationForm


class CustomerProfileView(generic.TemplateView):
    model = CustomerProfile
    template_name = 'accounts/index.html'


class StoreRegistrationView(generic.FormView):
    form_class = UserCreationForm
    template_name = 'account/store_registration.html'
    success_url = reverse_lazy('store_profile')

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('store_dashboard')
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user,
                  backend=settings.AUTHENTICATION_BACKENDS[0])
        return super(StoreRegistrationView, self).form_valid(form)


class UserLoginView(generic.FormView):
    form_class = CustomAuthentication
    template_name = 'account/store_login.html'
    redirect_authenticated_user = True
    redirect_field_name = 'next'
    
    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return reverse_lazy('store_dashboard')
        return super().get(request, *args, **kwargs)
    
    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user.is_active:
            login(self.request, user, backend=settings.AUTHENTICATION_BACKENDS[0])
            return redirect('store_dashboard')
        