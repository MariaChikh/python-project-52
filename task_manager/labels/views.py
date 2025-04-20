from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from task_manager.labels.models import Label
from task_manager.labels.forms import LabelCreationForm, LabelChangeForm
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from task_manager.tasks.models import Task


class IndexView(LoginRequiredMixin, ListView):
    model = Label
    template_name = 'labels/index.html'
    context_object_name = 'labels'


class LabelCreateView(LoginRequiredMixin, CreateView):
    form_class = LabelCreationForm
    template_name = 'labels/create.html'
    success_url = reverse_lazy('labels_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_update'] = False
        return context
    
    def form_valid(self, form):
        messages.success(self.request, _("Label successfully created"))
        return super().form_valid(form)
    

class LabelUpdateView(LoginRequiredMixin, UpdateView):
    model = Label
    form_class = LabelChangeForm
    template_name = 'labels/create.html'
    success_url = reverse_lazy('labels_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_update'] = True
        return context
    
    def form_valid(self, form):
        messages.success(self.request, _("Label successfully updated"))
        return super().form_valid(form)
    

class LabelDeleteView(LoginRequiredMixin, DeleteView):
    model = Label
    template_name = 'labels/delete.html'
    success_url = reverse_lazy('labels_index')
    context_object_name = 'label'

    def form_valid(self, form):
        label = self.get_object()
        if label.task_set.exists():
            messages.error(self.request, _('Cannot delete label because it is in use'))
            return redirect(self.success_url)
        messages.success(self.request, _('Label successfully deleted'))
        return super().form_valid(form)

