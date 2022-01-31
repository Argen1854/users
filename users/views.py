from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, ListView
from django.urls import reverse

from users.forms import LoginForm, RegistretionForm



class Registretion(CreateView):
    form_class = RegistretionForm
    success_url = '/users/'
    template_name = 'regis.html'


class NewLoginView(LoginView):
    form_class = LoginForm
    template_name = 'login.html'

    def get_success_url(self) -> str:
        return reverse('users:user_list')

class UserListView(ListView):
    queryset = User.objects.all()
    template_name = 'user_list.html'

    def get_queryset(self):
        return super().get_queryset()


