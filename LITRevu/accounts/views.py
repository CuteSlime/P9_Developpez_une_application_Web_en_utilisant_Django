from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import CreateView, View
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('flux')
    template_name = "registration/signup.html"


class HomeView(View):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('flux')
        else:
            return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return render(request, 'home.html', {

            'login_form': AuthenticationForm(),
        })
