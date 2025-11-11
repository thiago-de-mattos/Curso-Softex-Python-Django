from django.shortcuts import render
from .models import Tarefa, Execucao

def home(request):
    todas_as_execucoes = Execucao.objects.all()
    todas_as_tarefas = Tarefa.objects.all()
    context = {
        'nome_usuario': 'Thiago',
        'tecnologias': ['Python', 'Django', 'HTML', 'CSS'],
        'tarefas': todas_as_tarefas,
        'execucoes': todas_as_execucoes,
    }
    return render(request, 'home.html', context)


def login(request):
    return render(request, 'login.html')
