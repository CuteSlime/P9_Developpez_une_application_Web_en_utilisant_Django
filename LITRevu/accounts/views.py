from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import CreateView, View
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home')
    template_name = "registration/signup.html"


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home.html', {

            'login_form': AuthenticationForm(),
        })
