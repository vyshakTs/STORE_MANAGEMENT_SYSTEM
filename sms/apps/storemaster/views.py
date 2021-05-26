from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .forms import StoreCreationForm
from .models import WebStore


# Create your views here.
class StoreProfileCreationView(LoginRequiredMixin, generic.FormView):
    form_class = StoreCreationForm
    model = WebStore
    template_name = 'storemaster/store_profile.html'
    success_url = 'dashboard'
    
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['initial'] = {
            'user': self.request.user,
        }
        return kwargs
    
    
    def form_valid(self, form):
        profile = form.save()
        if profile is not None:
            login(self.request, profile, backend=settings.AUTHENTICATION_BACKENDS[0])
        return super(StoreProfileCreationView, self).form_valid(form)
    

class StoreProfileView(generic.TemplateView):
    template_name = 'storemaster/index.html'