from django.urls import path
from .views import ListaTarefasAPIView, EstatisticasTarefasAPIView

app_name = 'core'
urlpatterns = [
    path('tarefas/', ListaTarefasAPIView.as_view(), name='lista-tarefas'),
    path('tarefas/estatisticas/', EstatisticasTarefasAPIView.as_view(), name='estatisticas'),
]