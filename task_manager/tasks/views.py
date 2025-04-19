from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from task_manager.tasks.models import Task
from task_manager.tasks.forms import TaskCreationForm, TaskChangeForm
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages


class IndexView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks/index.html'
    context_object_name = 'tasks'


class TaskCreateView(LoginRequiredMixin, CreateView):
    form_class = TaskCreationForm
    template_name = 'tasks/create.html'
    success_url = reverse_lazy('tasks_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_update'] = False
        return context
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, _("Task successfully created"))
        return super().form_valid(form)
    

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskChangeForm
    template_name = 'tasks/create.html'
    success_url = reverse_lazy('tasks_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_update'] = True
        return context
    
    def form_valid(self, form):
        messages.success(self.request, _("Task successfully updated"))
        return super().form_valid(form)
    

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'tasks/delete.html'
    context_object_name = 'task'
    success_url = reverse_lazy('tasks_index')
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user)

    def dispatch(self, request, *args, **kwargs):
        task = self.get_object()
        if task.author != request.user:
            messages.error(request, _('A task can only be deleted by its author.'))
            return redirect('tasks_index')
        messages.success(self.request, _('Task successfully deleted'))
        return super().dispatch(request, *args, **kwargs)