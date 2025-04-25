import django_filters
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from task_manager.labels.models import Label
from task_manager.statuses.models import Status

from .models import Task


class TaskFilter(django_filters.FilterSet):
    status = django_filters.ModelChoiceFilter(
        queryset=Status.objects.all(),
        label= _('Status'),
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    executor = django_filters.ModelChoiceFilter(
        queryset=User.objects.all(),
        label=_('Executor'),
        widget=forms.Select(attrs={'class': 'form-select'}),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form.fields["executor"].label_from_instance = lambda obj: \
            f"{obj.first_name} {obj.last_name}"
        
    labels = django_filters.ModelMultipleChoiceFilter(
        queryset=Label.objects.all(),
        label=_('Labels'),
        widget=forms.CheckboxSelectMultiple(attrs={
            'class': 'form-check', 
            'size': '4'})
    )
    user_tasks = django_filters.BooleanFilter(
        method='user_tasks_filter',
        label=_('Only your tasks'),
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )

    class Meta:
        model = Task
        fields = ['status', 'executor', 'labels', 'user_tasks']       

    def user_tasks_filter(self, queryset, name, value):
        if value:
            return queryset.filter(author=self.request.user)
        return queryset.all()