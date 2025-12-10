from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Tarefa
from .serializers import TarefaSerializer
from django.db import IntegrityError
import logging
from django.db.models import Count, Q
from django.shortcuts import get_object_or_404

logger = logging.getLogger(__name__)


class ListaTarefasAPIView(APIView):
    
    
    def get(self, request, format=None):
        tarefas = Tarefa.objects.all()
        serializer = TarefaSerializer(tarefas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):

        try:
            serializer = TarefaSerializer(data=request.data)
            
            if serializer.is_valid():
                serializer.save()
                logger.info(f"[INFO]: Tarefa criada: {serializer.data['id']}")
                return Response(
                    serializer.data,
                    status=status.HTTP_201_CREATED
                )
            logger.warning(f"[WARNING]: Validação falhou: {serializer.errors}")
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

        except IntegrityError:
            return Response(
                {'error': '[ERROR]: Violação de integridade no banco de dados.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        except Exception as e:
            logger.error(f"Erro ao criar tarefa: {str(e)}")
            return Response(
                {'error': 'Erro interno do servidor.'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class EstatisticasTarefasAPIView(APIView):


    def get(self, request, format=None):

        try:

            tarefas = Tarefa.objects.all()


            stats = tarefas.aggregate(
                total=Count('id'),
                concluidas=Count('id', filter=Q(concluida=True)),
                pendentes=Count('id', filter=Q(concluida=False)),
            )

            total = stats['total']
            concluidas = stats['concluidas']

            resultado = {
                'total': total,
                'concluidas': concluidas,
                'pendentes': stats['pendentes'],
                'taxa_conclusao': round(concluidas / total, 2) if total > 0 else 0
            }

            return Response(resultado, status=status.HTTP_200_OK)

        except Exception as e:
            logger.error(f"Erro ao gerar estatísticas: {str(e)}")
            return Response(
                {'error': 'Erro ao gerar estatísticas.'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        
class DetalheTarefaAPIView(APIView):
    def get_object(self, pk):
        """
        Busca a tarefa pelo ID e retorna 404 se não encontrada.
        """
        return get_object_or_404(Tarefa, pk=pk)
  
    def get(self, request, pk, format=None):
        """
        Retorna os dados de uma tarefa específica.
        Args:
        pk: ID da tarefa na URL
        Returns:
        200 OK: Tarefa encontrada
        404 Not Found: Tarefa não existe
        """
        # 1. BUSCAR: Usa método auxiliar (trata 404)
        tarefa = self.get_object(pk)
        # 2. SERIALIZAR: Converte objeto único (sem many=True)
        serializer = TarefaSerializer(tarefa)
        # 3. RESPONDER: Retorna JSON com status 200
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk, format=None):
        """
        Atualiza tarefa completamente (substituição total).
        Exige que TODOS os campos editáveis sejam enviados.
        """
        # 1. BUSCAR: Obter o objeto existente
        tarefa = self.get_object(pk)
        # 2. SERIALIZAR: Passar objeto antigo E novos dados
        serializer = TarefaSerializer(tarefa, data=request.data)
        # ^^^^^ ^^^^^^^^^^^^^^^^
        # | Nova versão
        # Versão atual
        # 3. VALIDAR: Checar se JSON está completo e válido
        if serializer.is_valid():
            # 4. SALVAR: Atualizar no banco
            serializer.save()
            # 5. RESPONDER: Retornar objeto atualizado
            return Response(serializer.data, status=status.HTTP_200_OK)
            # ERRO: Retornar erros de validação
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        """
        Atualiza tarefa parcialmente (merge).
        Permite enviar apenas os campos que serão modificados.
        """
        # 1. BUSCAR: Obter o objeto existente
        tarefa = self.get_object(pk)
        # 2. SERIALIZAR: Passar objeto, novos dados E partial=True
        serializer = TarefaSerializer(tarefa,data=request.data,partial=True)
        # 3. VALIDAR
        if serializer.is_valid():
            # 4. SALVAR (aplica apenas os campos recebidos)
            serializer.save()
            # 5. RESPONDER
            return Response(serializer.data, status=status.HTTP_200_OK)
            # ERRO
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        """
        Remove um recurso específico.
        """
        # 1. BUSCAR: Obter o objeto (trata 404 se não existir)
        tarefa = self.get_object(pk)
        # 2. DELETAR
        tarefa.delete()
        # 3. RESPONDER: 204 No Content (sucesso sem corpo de resposta)
        return Response(status=status.HTTP_204_NO_CONTENT)