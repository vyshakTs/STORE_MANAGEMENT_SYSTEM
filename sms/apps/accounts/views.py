# Create your views here.
from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic

from apps.customers.models import CustomerProfile

from .forms import UserCreationForm


class CustomerProfileView(generic.TemplateView):
    model = CustomerProfile
    template_name = 'accounts/index.html'


class StoreRegistrationView(generic.FormView):
    form_class = UserCreationForm
    template_name = 'account/store_registration.html'
    success_url = reverse_lazy('store_profile')

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(settings.LOGIN_REDIRECT_URL)
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user,
                  backend=settings.AUTHENTICATION_BACKENDS[0])
        return super(StoreRegistrationView, self).form_valid(form)


class UserLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'account/user_login.html'
    redirect_authenticated_user = True
    redirect_field_name = 'next'
    success_url = 'home'
    
    def get_success_url(self):
        if self.request.user.is_authenticated:
            return reverse_lazy('home')
        return super().get_success_url()
