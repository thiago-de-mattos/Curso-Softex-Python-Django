from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Tarefa
from .serializers import TarefaSerializer
from django.db import IntegrityError
import logging
from django.db.models import Count, Q

logger = logging.getLogger(__name__)


class ListaTarefasAPIView(APIView):

    def get(self, request, format=None):
        tarefas = Tarefa.objects.all()
        serializer = TarefaSerializer(tarefas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):

        try:
            serializer = TarefaSerializer(data=request.data, context={'request': request})
            
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