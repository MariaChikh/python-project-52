from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.models import User
from task_manager.users.forms import CustomUserCreationForm, CustomUserChangeForm
from django.utils.translation import gettext_lazy as _
from task_manager.tasks.models import Task


class IndexView(ListView):
    model = User
    template_name = 'users/index.html'
    context_object_name = 'users'


class UserCreateView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('users_index')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_update'] = False
        return context
    
    def form_valid(self, form):
        messages.success(self.request, "Пользователь успешно зарегистрирован")
        return super().form_valid(form)
    
class UserUpdateView(UpdateView):
    model = User
    form_class = CustomUserChangeForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('users_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_update'] = True
        return context
    
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj != request.user:
            messages.error(request, _("You do not have permission to modify another user."))
            return redirect('users_index')
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        messages.success(self.request, _('User successfully changed'))
        return super().form_valid(form)
    
    
class UserDeleteView(DeleteView):
    model = User
    template_name = 'users/delete.html'
    success_url = reverse_lazy('users_index')
    context_object_name = 'user'

    #def dispatch(self, request, *args, **kwargs):
        
        #return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        obj = self.get_object()
        if obj != self.request.user:
            messages.error(self.request, _("You do not have permission to delete another user."))
            return redirect('users_index')
        if obj.tasks_created.exists():
            messages.error(self.request, _('Cannot delete user because it is in use'))
            return redirect(self.success_url)
        messages.success(self.request, _('User successfully deleted'))
        return super().form_valid(form)

