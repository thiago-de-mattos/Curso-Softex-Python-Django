from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Tarefa
from .serializers import TarefaSerializer
from rest_framework.exceptions import ValidationError
from django.db import IntegrityError
import logging

logger = logging.getLogger(__name__)

class ListaTarefasAPIView(APIView):
    def post(self, request, format=None):
        try:
            serializer = TarefaSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(
                    serializer.data,
                        status=status.HTTP_201_CREATED
                )

            return Response(
                serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST
            )
        except IntegrityError as e:
            # Erro de constraint no banco (ex: UNIQUE)
            return Response(
                {'error': 'Violação de integridade no banco de dados.'},
                    status=status.HTTP_400_BAD_REQUEST
            )

        except Exception as e:
            # Erro inesperado
            return Response(
                {'error': 'Erro interno do servidor.'},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def get(self, request, format=None):
        """Lista todas as tarefas."""
        tarefas = Tarefa.objects.all()
        serializer = TarefaSerializer(tarefas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        """
        Cria uma nova tarefa.

        Args:
        request.data: JSON com dados da tarefa
        {
        "titulo": "string",
        "concluida": boolean (opcional, default=False)
        }

        Returns:
        201 Created: Tarefa criada com sucesso
        400 Bad Request: Dados inválidos
        """
        # 1. INSTANCIAR: Criar serializer com dados recebidos
        serializer = TarefaSerializer(data=request.data)

        # 2. VALIDAR: Checar se os dados são válidos
        if serializer.is_valid():
            # 3. SALVAR: Persistir no banco de dados
            serializer.save()

            # 4. RESPONDER: Retornar objeto criado + status 201
            return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
            )

        # 5. ERRO: Retornar erros de validação + status 400
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
        

