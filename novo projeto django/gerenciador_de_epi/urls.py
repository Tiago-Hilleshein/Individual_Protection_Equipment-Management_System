from django.urls import path
from . import views # Isso importa as views (funções) do meu App

urlpatterns = [
    # path('', views.pagina_inicial, name='index')
    # O caminho vazio (o index do App) chama a função pagina_inicial
    path('', views.pagina_inicial, name='index'),
    path('cadastro/', views.cadastrar_colaborador, name='cadastrar_colaborador'),
    path('editar/<int:pk>/', views.editar_colaborador, name='editar_colaborador'),
    path('deletar/<int:pk>/', views.deletar_colaborador, name='deletar_colaborador'),
]