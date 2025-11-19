from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm # 1. Importe o form
from django.contrib.auth import login # 2. Importe a função 'login'
from django.contrib.auth.decorators import login_required # 1. Importe o decorador
from .models import Tarefa
from .forms import TarefaForm

@login_required
def home(request):
    if request.method == 'POST':
        # Cria uma instância do form e preenche com os dados do POST
        form = TarefaForm(request.POST)
        # 4. O Django valida os dados (max_length, etc.)
        if form.is_valid():
            # 'commit=False' cría o objeto na memória, mas não salva no banco.
            tarefa = form.save(commit=False)
            # 6. Redireciona de volta para a 'home' 
            # Isso é o Padrão "Post-Redirect-Get" (PRG)
            # Atribui o usuário logado (request.user) ao campo 'user' da tarefa
            tarefa.user = request.user
            # Agora sim, salva o objeto completo no banco
            tarefa.save()
            return redirect('home')
        # Se o form NÃO for válido, o código continua e
        # o 'form' (com os erros) será enviado para o template
    else:
        # 7. Lógica de GET: Se o usuário apenas visitou a página
        form = TarefaForm()  # Cria um formulário vazio

    # 8. A busca de dados (fora dos 'ifs', pois é necessária sempre)
    todas_as_tarefas = Tarefa.objects.filter(user=request.user).order_by('-criada_em')  # Ordena pelas mais novas

    # 9. Atualize o contexto para incluir o formulário
    context = {
        'nome_usuario': 'Thiago',
        'tecnologias': ['Python', 'Django', 'HTML', 'CSS'],
        'tarefas': todas_as_tarefas,
        'form': form,
    }

    return render(request, 'home.html', context)

@login_required
def concluir_tarefa(request, pk):
    # 2. Modifique o 'get_object_or_404'
    # Busque a Tarefa pela 'pk' E ONDE o 'user' é o 'request.user'
    tarefa = get_object_or_404(Tarefa, pk=pk, user=request.user)
    if request.method == 'POST':
        tarefa.concluida = True
        tarefa.save() # Não se esqueça de salvar!
    return redirect('home')

@login_required
def deletar_tarefa(request, pk):
    # 1. Busca a tarefa
    tarefa = get_object_or_404(Tarefa, pk=pk, user=request.user)
    # 2. Segurança: Apenas execute se o método for POST
    if request.method == 'POST':
        # 3. A Lógica de "Delete"
        tarefa.delete()
        # 4. Redireciona de volta para a 'home'
        return redirect('home')

def register(request):
    # Se a requisição for POST, o usuário enviou o formulário
    if request.method == 'POST':
        # Cria uma instância do formulário com os dados enviados
        form = UserCreationForm(request.POST)
        # Verifica se o formulário é válido (ex: senhas batem, username não existe)
        if form.is_valid():
            user = form.save() # Salva o novo usuário no banco
            login(request, user) # Faz o login automático do usuário
            return redirect('home')# Redireciona para a home
    # Se a requisição for GET, o usuário apenas visitou a página
    else:
        form = UserCreationForm() # Cria um formulário de cadastro vazio

    # Prepara o contexto e renderiza o template
    context = {'form': form}
    return render(request, 'register.html', context)


