from django.conf import settings
from django.contrib.auth import login
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from .forms import StoreCreationForm
from .models import WebStore


# Create your views here.
class StoreProfileCreationView(LoginRequiredMixin, generic.FormView):
    form_class = StoreCreationForm
    model = WebStore
    template_name = 'storemaster/store_profile.html'
    success_url = reverse_lazy('store_dashboard')
    
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
        return super(StoreProfileCreationView, self).form_valid(form)
    

class StoreProfileView(generic.TemplateView):
    template_name = 'storemaster/store_dashboard.html'
    
    def get(self, request, *args, **kwargs):
        try :
            self.request.user.webstore
        except ObjectDoesNotExist:
            return redirect('store_profile')          
        return super().get(request, *args, **kwargs)
    
    # def get_context_data(self, **kwargs):
    #     pass