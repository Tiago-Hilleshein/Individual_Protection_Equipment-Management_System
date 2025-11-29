from django.urls import path
from . import views

urlpatterns = [
    # Rota principal: Dashboard (nome da rota: 'dashboard')
    path('', views.dashboard, name='dashboard'), 
    
    # Rota de Colaboradores (nome da rota: 'listar_colaboradores')
    path('colaboradores/', views.listar_colaboradores, name='listar_colaboradores'),
    
    # Rotas de CRUD
    path('cadastro/', views.cadastrar_colaborador, name='cadastrar_colaborador'), 
    path('editar/<int:pk>/', views.editar_colaborador, name='editar_colaborador'), 
    path('deletar/<int:pk>/', views.deletar_colaborador, name='deletar_colaborador'),
    
    # Rotas de Empréstimo
    path('emprestar/', views.registrar_emprestimo, name='registrar_emprestimo'), 
    path('emprestimos/', views.listar_emprestimos, name='listar_emprestimos'),
]