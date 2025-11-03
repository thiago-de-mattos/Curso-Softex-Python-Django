from django.shortcuts import render

# Create your views here.
def home(request):
# 1. Crie seu dicionário de contexto
    context = {
        'nome_usuario': 'Thiago',
        'tecnologias': ['Python', 'Django', 'HTML', 'CSS']
    }
    return render(request, 'home.html', context)

def login(request):
    return 