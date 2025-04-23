from django import forms
from django.contrib.auth.forms import (
    UserChangeForm,
    UserCreationForm,
)
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label=_("Password"),
        widget=forms.PasswordInput(attrs={'label': _('Password'), 
                                          'placeholder': _('Password'), 
                                          'class': 'form-control'}),
        help_text=_("Your password must contain at least 3 characters."),
    )

    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'label': _('Confirm Password'), 
                                          'placeholder': _('Confirm password'), 
                                          'class': 'form-control'}),
        help_text=_("Please enter the password again to confirm."),
    )
    class Meta:
        model = User
        fields = ('first_name', 
                  'last_name', 
                  'username', 
                  'password1', 
                  'password2')

        labels = {
            'first_name': _('First Name'),
            'last_name': _('Last Name'),
            'username': _('Username'),
        }

        help_texts = {
            'username': _(
                '''Required field. No more than 150 characters. 
                Only letters, numbers and symbols @/./+/-/_.'''
            ),
        }
        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': _('Username'),
                'class': 'form-control',
            }),
            'first_name': forms.TextInput(attrs={
                'placeholder': _('First name'),
                'class': 'form-control',
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': _('Last name'),
                'class': 'form-control',
            }),
        }

    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        if password1 and len(password1) < 3:
            raise forms.ValidationError(_('''Your password must contain
                                        at least 3 characters.'''))
        return password1
    
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(_("Passwords doesn't match"))
        return cleaned_data
    
    def _post_clean(self):
        super(forms.ModelForm, self)._post_clean() 
    

class CustomUserChangeForm(UserChangeForm):
    password = None 
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username']

        labels = {
            'first_name': _('First Name'),
            'last_name': _('Last Name'),
            'username': _('Username'),
        }

        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': _('Name'),
                'class': 'form-control',
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': _('Last Name'),
                'class': 'form-control'
            }),
            'username': forms.TextInput(attrs={
                'placeholder': _('Username'),
                'class': 'form-control'
            }),
        }