from django.urls import path
from . import views as v

urlpatterns = [
    path('login-signup', v.login_signup, name='login-signup'),
]
