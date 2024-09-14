# projetos/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('projetos/', views.lista_projetos, name='lista_projetos'),
    path('projetos/submeter/', views.submeter_projeto, name='submeter_projeto'),
    path('projetos/<int:projeto_id>/', views.detalhes_projeto, name='detalhes_projeto'),
    path('notas/', views.historico_notas, name='historico_notas'),
]
