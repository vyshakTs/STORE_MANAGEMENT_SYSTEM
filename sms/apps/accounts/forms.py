# from allauth.account.forms import SignupForm
from django import forms
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.utils.translation import gettext_lazy as _

from sms.apps.storemaster.models import WebStore

from .models import User


class CustomAuthentication(AuthenticationForm):
    username = forms.CharField(
        label=_('Username'), widget=forms.TextInput,
    )
    password = forms.CharField(
        label=_('Password'), widget=forms.PasswordInput,
    )
    
    class Meta:
        model = User
        fields = ('username', 'password')
        
    def __init__(self, *args, **kwargs):
        self.valid_user = None
        super().__init__(*args, **kwargs)
        
    def _post_clean(self):
        super()._post_clean()
        
        password = self.cleaned_data.get('password', '')
        
    def clean_username(self):
        username = self.cleaned_data.get('username', '')
        try:
            self.valid_user = User.objects.get(Q(username=username)|Q(email=username))
        except ObjectDoesNotExist:
            raise forms.ValidationError(
                _('Account with the given username does not exists.')
            )
        return username
    
    def clean_password(self):
        username = self.cleaned_data.get('username', '')
        password = self.cleaned_data.get('password', '')
        if self.valid_user:
            if not self.valid_user.check_password(password) :
                raise forms.ValidationError(
                    _('Password entered is incorrect.')
                )
        return password
    


class UserCreationForm(forms.ModelForm):
    username = forms.CharField(
        label=_('Username'), widget=forms.TextInput,
    )
    first_name = forms.CharField(
        label=_('First name'), widget=forms.TextInput
    )
    last_name = forms.CharField(
        label=_('Last name'), widget=forms.TextInput
    )
    email = forms.EmailField(label=_('Email address'))
    password1 = forms.CharField(
        label=_('Password'), widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label=_('Confirm password'), widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name', 'last_name',
            'password1', 'password2',
        )

    def __init__(self, *args, **kwargs):
        self.user_type = kwargs['initial'].get('user_type', '')
        super().__init__(*args, **kwargs)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError(
                _('A user with that email address already exits.')
            )
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError(
                _('A user with that username already exits.')
            )
        return username

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError(
                _("The two password fields didn't match")
            )
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password1'))
        if self.user_type == User.STORE_OWNER:
            user.user_type = User.STORE_OWNER
        elif self.user_type == User.EMPLOYEE:
            user.user_type = User.EMPLOYEE
        else:
            user.user_type = User.CUSTOMER
        if commit:
            user.save()
        return user
