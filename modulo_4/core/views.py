from django.shortcuts import render
from .models import Tarefa, Execucao

def home(request):
    todas_as_execucao = Execucao.objects.all()
    todas_as_tarefas = Tarefa.objects.all()
    context = {
        'nome_usuario': 'Thiago',
        'tecnologias': ['Python', 'Django', 'HTML', 'CSS'],
        'tarefas': todas_as_tarefas,
        'execucao': todas_as_execucao

    }
    return render(request, 'home.html', context)

def login(request):
    return 