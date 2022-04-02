from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView

from account.forms import RegistrationForm

User = get_user_model()

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
    def get(self, request, activation_code):
        # user = User.objects.get(activation_code=activation_code)
        user = get_object_or_404(User, activation_code=activation_code)
        user.is_active = True
        user.activation_code = ''
        user.save()
        return render(request, 'account/activation.html', {})


class SignInView(LoginView):
    template_name = 'account/login.html'




class ChangePasswordView(View):
    def post(self, request):
        pass


class ForgotPasswordView(View):
    def post(self, request):
        pass





