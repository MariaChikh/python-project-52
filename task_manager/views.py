import rollbar
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'


class CustomLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

    def form_valid(self, form):
        messages.success(self.request, _("You are logged in"))
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 
                       _('''Please enter a valid username and password. 
                            Both fields may be case sensitive.'''))
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('index')


class CustomLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        messages.info(request, _('You are logged out'))
        return super().dispatch(request, *args, **kwargs)
    

def test_rollbar(request):
    try:
        1 / 0
    except Exception:
        rollbar.report_exc_info()  

    return HttpResponse("Test Rollbar Error")
