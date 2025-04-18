from django.contrib import messages
from django.views.generic import ListView, CreateView
from task_manager.statuses.models import Status
from task_manager.statuses.forms import StatusCreationForm
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy


class IndexView(ListView):
    model = Status
    template_name = 'statuses/index.html'
    context_object_name = 'statuses'


class StatusCreateView(CreateView):
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