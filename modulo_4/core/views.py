from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarefa, Execucao
from .forms import TarefaForm

def home(request):
    if request.method == 'POST':
        # Cria uma instância do form e preenche com os dados do POST
        form = TarefaForm(request.POST)
        # 4. O Django valida os dados (max_length, etc.)
        if form.is_valid():
            # 5. Salva o objeto no banco de dados!
            form.save()
            # 6. Redireciona de volta para a 'home' 
            # Isso é o Padrão "Post-Redirect-Get" (PRG)
            return redirect('home')
        # Se o form NÃO for válido, o código continua e
        # o 'form' (com os erros) será enviado para o template
    else:
        # 7. Lógica de GET: Se o usuário apenas visitou a página
        form = TarefaForm()  # Cria um formulário vazio

    # 8. A busca de dados (fora dos 'ifs', pois é necessária sempre)
    todas_as_tarefas = Tarefa.objects.all().order_by('-criada_em')  # Ordena pelas mais novas
    todas_as_execucoes = Execucao.objects.all()

    # 9. Atualize o contexto para incluir o formulário
    context = {
        'nome_usuario': 'Thiago',
        'tecnologias': ['Python', 'Django', 'HTML', 'CSS'],
        'tarefas': todas_as_tarefas,
        'execucoes': todas_as_execucoes,
        'form': form,
    }

    return render(request, 'home.html', context)

def concluir_tarefa(request, pk):
    
    tarefa = get_object_or_404(Tarefa, pk=pk)
    # 2. Segurança: Apenas execute se o método for POST
    if request.method == 'POST':
        # 3. A Lógica de "Update"
        tarefa.concluida = True
        tarefa.save() # Não se esqueça de salvar!
        # 4. Redireciona de volta para a 'home' (Padrão PRG)
        return redirect('home')

def deletar_tarefa(request, pk):
    # 1. Busca a tarefa
    tarefa = get_object_or_404(Tarefa, pk=pk)
    # 2. Segurança: Apenas execute se o método for POST
    if request.method == 'POST':
        # 3. A Lógica de "Delete"
        tarefa.delete()
        # 4. Redireciona de volta para a 'home'
        return redirect('home')

def login(request):
    return render(request, 'login.html')
