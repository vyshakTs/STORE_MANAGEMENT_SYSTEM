# from allauth.account.forms import SignupForm
from django import forms
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.utils.translation import gettext_lazy as _

from apps.storemaster.models import WebStore

from .models import User


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
        super().__init__(*args, **kwargs)

    def _post_clean(self):
        super()._post_clean()
        password = self.cleaned_data.get('password2')
        username = self.cleaned_data.get('username')
        # Validate after self.instance is updated with form data
        # otherwise validators can't access email
        if password:
            try:
                validate_password(password, self.instance)
            except forms.ValidationError as error:
                self.add_error('password2', error)

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
        user.user_type = User.STORE_OWNER
        if commit:
            user.save()
        return user
