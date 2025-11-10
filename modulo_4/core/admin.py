from django.contrib import admin
from .models import Tarefa,Execucao

# Register your models here.
admin.site.register(Tarefa)
admin.site.register(Execucao)