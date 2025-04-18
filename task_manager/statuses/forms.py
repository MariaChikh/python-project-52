from django import forms
from .models import Status
from django.utils.translation import gettext_lazy as _


class StatusCreationForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['name']

        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': _('Username'),
                'class': 'form-control',
            })
        }
