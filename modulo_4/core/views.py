from django.shortcuts import render
from .models import Tarefa
# Create your views here.
def home(request):

    todas_as_tarefas = Tarefa.objects.all()
    context = {
        'nome_usuario': 'Thiago',
        'tecnologias': ['Python', 'Django', 'HTML', 'CSS'],
        'tarefas': todas_as_tarefas
    }
    return render(request, 'home.html', context)

def login(request):
    return 