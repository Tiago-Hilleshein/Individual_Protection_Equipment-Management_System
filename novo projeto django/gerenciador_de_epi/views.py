# gerenciador_de_epi/views.py

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404 # ⬅️ Adicionamos o 'redirect'
from .models import Colaborador
from .forms import ColaboradorForm # Importação do formulário

@login_required
def pagina_inicial(request):
    colaboradores = Colaborador.objects.all() 

    contexto = {
        'lista_colaboradores': colaboradores 
    }
    return render(request, 'gerenciador_de_epi/index.html', contexto)


@login_required
def cadastrar_colaborador(request):
    """
    View para exibir e processar o formulário de cadastro de Colaborador.
    """
    if request.method == 'POST':
        # 1. Se os dados foram enviados, preenchemos o formulário
        form = ColaboradorForm(request.POST)
        
        if form.is_valid():
            # 2. Se os dados estiverem corretos, salvamos no banco
            form.save()
            
            # 3. Redirecionamos para a lista de colaboradores (rota 'index')
            return redirect('/gerenciar/') 
    else:
        # Se for um acesso direto (GET), criamos um formulário vazio
        form = ColaboradorForm()
        
    contexto = {'form': form}
    return render(request, 'gerenciador_de_epi/colaborador_form.html', contexto)
@login_required
def editar_colaborador(request, pk):
    """
    View para buscar, exibir e salvar a edição de um Colaborador.
    """
    # 1. Busca o objeto Colaborador pelo ID (pk). 
    # Se não encontrar, mostra a página 404.
    colaborador = get_object_or_404(Colaborador, pk=pk)
    
    if request.method == 'POST':
        # 2. Preenche o formulário com os dados POST E INFORMA O OBJETO A SER ATUALIZADO (instance)
        form = ColaboradorForm(request.POST, instance=colaborador)
        
        if form.is_valid():
            # 3. O save() atualiza o objeto existente (não cria um novo)
            form.save()
            return redirect('index') # Redireciona para a lista após a edição
    else:
        # 4. Se for GET, preenche o formulário com os dados ATUAIS do objeto
        form = ColaboradorForm(instance=colaborador)
        
    contexto = {'form': form}
    # Reutilizamos o mesmo template de formulário de cadastro
    return render(request, 'gerenciador_de_epi/colaborador_form.html', contexto)
@login_required
def deletar_colaborador(request, pk):
    # 1. Busca o objeto Colaborador pelo ID. Se não encontrar, mostra 404.
    colaborador = get_object_or_404(Colaborador, pk=pk)

    # 2. A deleção só deve ocorrer se o método for POST (enviado por um formulário)
    if request.method == 'POST':
        colaborador.delete() # Comando direto para remover do banco
        print("Deletado com sucesso!")
        
        # 3. Redireciona de volta para a lista (página inicial)
        return redirect('index')

    # Se o método não for POST, renderizamos um template de confirmação (próximo passo)
    contexto = {'colaborador': colaborador}
    return render(request, 'gerenciador_de_epi/colaborador_confirm_delete.html', contexto)