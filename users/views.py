from . import forms
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import auth
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required


class SignUpView(FormView):

    template_name = "users/signup.html"
    form_class = forms.SignUpForm
    success_url = reverse_lazy("core:home")

    def form_valid(self, form):
        form.save()
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)


def login_view(request):
    form = forms.LoginForm()
    if request.method == "POST":
        form = forms.LoginForm(request.POST)
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        get_user = auth.authenticate(request, username=username, password=password)
        if get_user is not None:
            auth.login(request, get_user)
            return redirect("/")
        else:
            return render(request, "users/login.html", {"form": form})
            # return redirect(reverse("users:login"))
    elif request.method == "GET":
        form = forms.LoginForm()
        return render(request, "users/login.html", {"form": form})


@login_required(login_url="/users/login/")
def log_out(request):
    logout(request)
    return redirect(reverse("core:home"))
