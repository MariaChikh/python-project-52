from django import forms
from .models import Status
from django.utils.translation import gettext_lazy as _


class StatusCreationForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['name']

        labels = {
            'name': _('Name'),
        }

        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': _('Name'),
                'class': 'form-control',
            })
        }


class StatusChangeForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['name']

        labels = {
            'name': _('Name'),
        }

        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': _('Name'),
                'class': 'form-control',
            })
        }
