from django import forms
from .models import Task
from task_manager.statuses.models import Status
#from task_manager.labels.models import Label
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class TaskCreationForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor',]

        labels = {
            'name': _('Name'),
            'description': _('Description'),
            'status': _('Status'),
            'executor': _('Executor'),
            #'labels': _('Labels'),
        }

        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': _('Name'),
                'class': 'form-control',
            }),
            'description': forms.Textarea(attrs={
                'placeholder': _('Description'),
                'class': 'form-control',
            }),
            'status': forms.Select(attrs={
                'class': 'form-control',
            }),
            'executor': forms.Select(attrs={
                'class': 'form-control',
            }),
            #'labels': forms.SelectMultiple(attrs={
                #'class': 'form-control',
                #'size': '6',
            #}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['status'].queryset = Status.objects.all()
            self.fields['executor'].queryset = User.objects.all()
            #self.fields['labels'].queryset = Label.objects.all()


class TaskChangeForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor']

        labels = {
            'name': _('Name'),
            'description': _('Description'),
            'status': _('Status'),
            'executor': _('Executor'),
            #'labels': _('Labels'),
        }

        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': _('Name'),
                'class': 'form-control',
            }),
            'description': forms.Textarea(attrs={
                'placeholder': _('Description'),
                'class': 'form-control',
            }),
            'status': forms.Select(attrs={
                'class': 'form-control',
            }),
            'executor': forms.Select(attrs={
                'class': 'form-control',
            }),
            #'labels': forms.SelectMultiple(attrs={
                #'class': 'form-control',
                #'size': '6',
            #}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['status'].queryset = Status.objects.all()
            self.fields['executor'].queryset = User.objects.all()
            #self.fields['labels'].queryset = Label.objects.all()