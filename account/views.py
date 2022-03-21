from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView

from account.forms import RegistrationForm


class RegistrationView(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'account/registration.html', {'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(reverse_lazy('successful-registration'))
        return render(request, 'account/registration.html', {'form': form})


class SuccessfulRegistrationPage(TemplateView):
    template_name = 'account/successful_registration.html'


class ActivationView(View):
    def post(self, request):
        pass


class LoginView():
    pass


class LogoutView():
    pass


class ChangePasswordView(View):
    def post(self, request):
        pass


class ForgotPasswordView(View):
    def post(self, request):
        pass





