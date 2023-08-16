from django.urls import path
from . import views as v

urlpatterns = [
    path('try-me/<int:pk>', v.test_it, name='test'),
]
