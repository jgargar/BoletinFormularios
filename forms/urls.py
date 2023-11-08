from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('formulario_uno/', views.formulario_uno, name='formulario_uno'),
    path('formulario_dos/', views.formulario_dos, name='formulario_dos'),
    path('formulario_tres/', views.formulario_tres, name='formulario_tres')
]