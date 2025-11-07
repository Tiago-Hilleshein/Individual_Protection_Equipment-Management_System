# gerenciador_de_epi/views.py

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404 
# ⬅️ CORREÇÃO: Importar TODOS os modelos
from .models import Colaborador, EPI, Emprestimo 
from .forms import ColaboradorForm, EmprestimoForm 

# =======================================================
# DASHBOARD / PÁGINA INICIAL
# =======================================================
@login_required
def dashboard(request):
    """
    Exibe o Dashboard principal e a saudação.
    """
    return render(request, 'gerenciador_de_epi/dashboard.html')


# =======================================================
# LISTAGEM DE COLABORADORES (READ)
# =======================================================
@login_required
def listar_colaboradores(request):
    """
    Busca e lista todos os colaboradores.
    """
    colaboradores = Colaborador.objects.all() 

    contexto = {
        'lista_colaboradores': colaboradores 
    }
    return render(request, 'gerenciador_de_epi/colaboradores_lista.html', contexto)


# =======================================================
# CADASTRO DE COLABORADOR (CREATE)
# =======================================================
@login_required
def cadastrar_colaborador(request):
    """
    View para exibir e processar o formulário de cadastro de Colaborador.
    """
    if request.method == 'POST':
        form = ColaboradorForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('listar_colaboradores') # ⬅️ CORREÇÃO: Redirecionar para o nome da rota
    else:
        form = ColaboradorForm()
        
    contexto = {'form': form}
    return render(request, 'gerenciador_de_epi/colaborador_form.html', contexto)


# =======================================================
# EDIÇÃO DE COLABORADOR (UPDATE)
# =======================================================
@login_required
def editar_colaborador(request, pk):
    """
    View para buscar, exibir e salvar a edição de um Colaborador.
    """
    colaborador = get_object_or_404(Colaborador, pk=pk)
    
    if request.method == 'POST':
        # Instância informa ao ModelForm qual objeto atualizar
        form = ColaboradorForm(request.POST, instance=colaborador) 
        
        if form.is_valid():
            form.save()
            return redirect('listar_colaboradores') # ⬅️ CORREÇÃO: Redirecionar para o nome da rota
    else:
        # Preenche o formulário com os dados ATUAIS
        form = ColaboradorForm(instance=colaborador) 
        
    contexto = {'form': form}
    return render(request, 'gerenciador_de_epi/colaborador_form.html', contexto)


# =======================================================
# EXCLUSÃO DE COLABORADOR (DELETE)
# =======================================================
@login_required
def deletar_colaborador(request, pk):
    colaborador = get_object_or_404(Colaborador, pk=pk)

    if request.method == 'POST':
        colaborador.delete()
        print(f"Colaborador {colaborador.nome_completo} deletado com sucesso!")
        return redirect('listar_colaboradores') # ⬅️ CORREÇÃO: Redirecionar para o nome da rota

    contexto = {'colaborador': colaborador}
    return render(request, 'gerenciador_de_epi/colaborador_confirm_delete.html', contexto)


# =======================================================
# REGISTRO DE EMPRÉSTIMO (CREATE)
# =======================================================
@login_required
def registrar_emprestimo(request):
    """
    View para exibir e processar o formulário de registro de Empréstimo.
    """
    if request.method == 'POST':
        form = EmprestimoForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('listar_emprestimos') # ⬅️ Redirecionar para a lista de empréstimos
    else:
        form = EmprestimoForm()
        
    contexto = {'form': form}
    return render(request, 'gerenciador_de_epi/emprestimo_form.html', contexto)


# =======================================================
# LISTAGEM DE EMPRÉSTIMOS (READ)
# =======================================================
@login_required
def listar_emprestimos(request):
    """
    Busca todos os registros de Empréstimo, buscando também os dados relacionados de Colaborador e EPI.
    """
    emprestimos = Emprestimo.objects.select_related('colaborador', 'epi').all() 
    
    contexto = {
        'lista_emprestimos': emprestimos 
    }
    return render(request, 'gerenciador_de_epi/emprestimos_lista.html', contexto)