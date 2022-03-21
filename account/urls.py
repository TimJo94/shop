from django.urls import path

from .views import *


urlpatterns = [
    path('register/', RegistrationView.as_view(), name='registration'),
    path('successful_registration/', SuccessfulRegistrationPage.as_view(), name='successful-registration'),
    # path('activate/', ActivationView.as_view(), name='activation'),
    # path('login/', LoginView.as_view(), name='signup'),
    # path('logout/', LogoutView.as_view(), name='signout'),
    # path('change_password/', ChangePasswordView.as_view(), name='change-password'),
    # path('forgot_password', ForgotPasswordView.as_view(), name='forgot-password'),

]