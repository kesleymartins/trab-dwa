from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name="students.index"),
    path('aluno/<int:id>/matricula', views.matricula, name="students.matricula"),
    path('contato', views.contato, name="students.contato"),
]
