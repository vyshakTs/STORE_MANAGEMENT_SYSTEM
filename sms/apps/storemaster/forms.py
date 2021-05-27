from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import WebStore


class StoreCreationForm(forms.ModelForm):
    name = forms.CharField(
        label=_('Store name'), widget=forms.TextInput,
    )
    address1 = forms.CharField(
        label=_('address line 1'), widget=forms.TextInput,
    )
    address2 = forms.CharField(
        label=_('address line 2'), widget=forms.TextInput,
    )
    phone_no = forms.CharField(
        label=_('Phone number'), widget=forms.TextInput,
    )
    
    class Meta:
        model = WebStore
        exclude = ('user', 'store_id')
        
    def __init__(self, *args, **kwargs):
        self.user = kwargs['initial'].get('user')
        super().__init__(*args, **kwargs)
        
    def _post_clean(self):
        super()._post_clean()
        
    def save(self, commit=True, *args,**kwargs):
        profile = super().save(commit=False)
        profile.user = self.user
        if commit:
            profile.save()
        return profile
    
    