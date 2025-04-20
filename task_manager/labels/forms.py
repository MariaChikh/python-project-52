from django import forms
from .models import Label
from django.utils.translation import gettext_lazy as _


class LabelCreationForm(forms.ModelForm):
    class Meta:
        model = Label
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


class LabelChangeForm(forms.ModelForm):
    class Meta:
        model = Label
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
