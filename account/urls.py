from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import *


urlpatterns = [
    path('register/', RegistrationView.as_view(), name='registration'),
    path('successful_registration/', SuccessfulRegistrationPage.as_view(), name='successful-registration'),
    path('activate/<str:activation_code>/', ActivationView.as_view(), name='activation'),
    path('login/', SignInView.as_view(), name='signin'),
    path('logout/', LogoutView.as_view(), name='signout'),
    # path('change_password/', ChangePasswordView.as_view(), name='change-password'),
    # path('forgot_password', ForgotPasswordView.as_view(), name='forgot-password'),

]