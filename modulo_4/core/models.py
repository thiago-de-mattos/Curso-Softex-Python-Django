from django.db import models
from django.contrib.auth.models import User 

class Tarefa(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # 'on_delete=models.CASCADE' diz ao banco:
    # "Se o usuário for deletado, delete todas as tarefas dele também."
    titulo = models.CharField(max_length=200)
    concluida = models.BooleanField(default=False)
    criada_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    
