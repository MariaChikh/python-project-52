from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from task_manager.statuses.models import Status
from task_manager.statuses.forms import StatusCreationForm, StatusChangeForm
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from task_manager.tasks.models import Task


class IndexView(LoginRequiredMixin, ListView):
    model = Status
    template_name = 'statuses/index.html'
    context_object_name = 'statuses'


class StatusCreateView(LoginRequiredMixin, CreateView):
    form_class = StatusCreationForm
    template_name = 'statuses/create.html'
    success_url = reverse_lazy('statuses_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_update'] = False
        return context
    
    def form_valid(self, form):
        messages.success(self.request, _("Status successfully created"))
        return super().form_valid(form)
    

class StatusUpdateView(LoginRequiredMixin, UpdateView):
    model = Status
    form_class = StatusChangeForm
    template_name = 'statuses/create.html'
    success_url = reverse_lazy('statuses_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_update'] = True
        return context
    
    def form_valid(self, form):
        messages.success(self.request, _("Status successfully updated"))
        return super().form_valid(form)
    

class StatusDeleteView(LoginRequiredMixin, DeleteView):
    model = Status
    template_name = 'statuses/delete.html'
    success_url = reverse_lazy('statuses_index')
    context_object_name = 'status'

    def form_valid(self, form):
        status = self.get_object()
        if status.task_set.exists():
            messages.error(self.request, _('Cannot delete status because it is in use'))
            return redirect(self.success_url)
        messages.success(self.request, _('Status successfully deleted'))
        return super().form_valid(form)
