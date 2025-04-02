from django.urls import path
from . import views

app_name = "IMC"

urlpatterns = [
    path('', views.imc, name='imc')
]