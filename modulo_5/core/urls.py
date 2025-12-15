from django.urls import path
from .views import ListaTarefasAPIView, EstatisticasTarefasAPIView, DetalheTarefaAPIView, concluiTodasTarefas, LogoutView

app_name = 'core'
urlpatterns = [
    path('tarefas/', ListaTarefasAPIView.as_view(), name='lista-tarefas'),
    path('tarefas/estatisticas/', EstatisticasTarefasAPIView.as_view(), name='estatisticas'),
    path('tarefas/<int:pk>/duplicar/', DetalheTarefaAPIView.as_view()),
    path('tarefas/<int:pk>/',DetalheTarefaAPIView.as_view(),name='detalhe-tarefa'),
    path('tarefas/concluir-todas/', concluiTodasTarefas.as_view()),
    path('logout/', LogoutView.as_view(), name='logout'), # ← Novo endpoint
]