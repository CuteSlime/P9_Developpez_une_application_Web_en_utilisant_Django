from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import CreateView, View
from .forms import CustomUserCreationForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('flux')
    template_name = "registration/signup.html"

    def form_valid(self, form):
        valid = super().form_valid(form)
        username = self.request.POST['username']
        password = self.request.POST['password1']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(self.request, user)
            return redirect('flux')

        return valid


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

    def post(self, request, *args, **kwargs):
        login_form = AuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            login(request, login_form.get_user())
            return redirect('flux')
        else:
            return render(request, 'home.html', {'login_form': login_form})
