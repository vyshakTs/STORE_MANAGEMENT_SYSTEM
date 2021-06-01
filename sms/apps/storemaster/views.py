from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic

from .forms import StoreCreationForm
from .mixins import IsStoreOwnerMixin
from .models import WebStore


# Create your views here.
class StoreProfileCreationView(LoginRequiredMixin, IsStoreOwnerMixin, generic.FormView):
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
    

class StoreProfileView(LoginRequiredMixin, IsStoreOwnerMixin, generic.TemplateView):
    template_name = 'storemaster/store_dashboard.html'
    
    def get(self, request, *args, **kwargs):
        try :
            self.request.user.webstore
        except ObjectDoesNotExist:
            return redirect('store_profile')          
        return super().get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        # context['order_count'] = Orders.objects.filter(Q(webstore=self.request.user.webstore),
        #                             ~Q(status=Orders.INVALID)).count()
        # context['sales'] = Orders.objects.filter(Q(webstore=self.request.user.webstore), 
        #                         Q(status=Orders.COMPLETED)).count()
        # context['visitors'] = None
        return context