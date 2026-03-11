from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('verificar/', views.verificar_paridad, name='verificar'),
]