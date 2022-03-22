from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class RegistrationForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(min_length=6, widget=forms.PasswordInput, required=True)
    password_confirm = forms.CharField(min_length=6, widget=forms.PasswordInput, required=True)
    name = forms.CharField(required="True")
    last_name = forms.CharField(required="True")

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email has already been used')
        return email

    def clean(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.pop('password_confirm')
        if password1 != password2:
            raise forms.ValidationError('Passwords do not match')
        return self.cleaned_data

    def save(self):
        data = self.cleaned_data
        user = User.objects.create_user(**data)
        user.set_activation_code()
        # TODO: отправка писем на почту
        user.send_activation_mail()


# class LoginForm(forms.Form):
#     email = forms.EmailField()
#     password = forms.CharField(widget=forms.PasswordInput)
#     def clean_email(self):
#


class ChangePasswordForm(forms.Form):
    pass


class ForgotPasswordForm(forms.Form):
    pass
