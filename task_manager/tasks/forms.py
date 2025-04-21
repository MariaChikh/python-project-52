from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from task_manager.labels.models import Label
from task_manager.statuses.models import Status

from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'labels', 'executor',]

        labels = {
            'name': _('Name'),
            'description': _('Description'),
            'status': _('Status'),
            'executor': _('Executor'),
            'labels': _('Labels'),
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
            'labels': forms.CheckboxSelectMultiple(attrs={
                'class': 'form-check',
                'size': '4',
            }),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['status'].queryset = Status.objects.all()
            self.fields['executor'].queryset = User.objects.all()
            self.fields['labels'].queryset = Label.objects.all()
