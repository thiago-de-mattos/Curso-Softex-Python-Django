from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Tarefa
from .serializers import TarefaSerializer
from django.db import IntegrityError
import logging
from django.db.models import Count, Q
from django.shortcuts import get_object_or_404
from django.utils.timezone import now
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import TarefaSerializer, UserRegistrationSerializer
from django.contrib.auth.models import User
from rest_framework import generics
from .permissions import IsGerente 

logger = logging.getLogger(__name__)

class RegisterView(generics.CreateAPIView):
    """
    Endpoint para cadastro de novos usuários.
    Acesso: Público (Qualquer um pode criar conta).
    """
    queryset = User.objects.all()
    permission_classes = [AllowAny] # Sobrescreve o padrão global
    serializer_class = UserRegistrationSerializer



class TarefaListCreateAPIView(generics.ListCreateAPIView):

    serializer_class = TarefaSerializer
    permission_classes = [IsAuthenticated] # Exige Token válido

    def get_queryset(self):
        """
        Sobrescreve o comportamento padrão para retornar APENAS
        os dados pertencentes ao usuário logado.
        """
        # 1. Recupera o usuário validado pelo JWT
        user = self.request.user
        # 2. Retorna o filtro. O Django fará o WHERE user_id = X no banco.
        return Tarefa.objects.filter(user=user)
    
    def perform_create(self, serializer):
        # Garante que a tarefa criada seja vinculada ao usuário logado
        serializer.save(user=self.request.user)
    
    def post(self, request, format=None):

        try:
            serializer = TarefaSerializer(data=request.data)
            
            if serializer.is_valid():
                serializer.save(user=self.request.user)
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
        
class TarefaRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    
    serializer_class = TarefaSerializer
    
    def get_queryset(self):
        return Tarefa.objects.filter(user=self.request.user)
    
    def get_permissions(self):
        """
        Instancia e retorna a lista de permissões que esta view requer,
        dependendo do método HTTP da requisição.
        """
        if self.request.method == 'DELETE':
            # Para deletar: Precisa estar logado E ser Gerente
            # A ordem importa: primeiro checa login, depois o grupo
            return [IsAuthenticated(), IsGerente()]
        
        # Para GET, PUT, PATCH: Basta estar logado (e ser dono, garantido pelo queryset)
        return [IsAuthenticated()]

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
    
    def post(self, request, pk, format=None):

        if request.path.endswith("/duplicar/"):

            tarefa_original = self.get_object(pk)

            nova_tarefa = Tarefa.objects.create(
                user=tarefa_original.user,
                titulo=tarefa_original.titulo + " (cópia)",
                prioridade=tarefa_original.prioridade,
                prazo=tarefa_original.prazo,
                concluida=False,              
                data_conclusao=None           
            )

            serializer = TarefaSerializer(nova_tarefa)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(
            {"error": "Rota não encontrada."},
            status=status.HTTP_404_NOT_FOUND
        )
    
class concluiTodasTarefas(APIView):


    def patch(self, request, format=None):

        hoje = now().date()
        
        tarefas_atualizadas = Tarefa.objects.filter(
            concluida=False
        ).update(
            concluida=True,
            data_conclusao=hoje
        )

        return Response(
            {
                "mensagem": "Tarefas concluídas com sucesso.",
                "total_atualizadas": tarefas_atualizadas
            },
            status=status.HTTP_200_OK
        )
    
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        try:
            refresh_token = request.data.get("refresh")
            token = RefreshToken(refresh_token)
            token.blacklist() # Adiciona o token à lista negra

            return Response(
                {"detail": "Logout realizado com sucesso."},
                status=status.HTTP_205_RESET_CONTENT # 205 é a resposta padrão para "reset content"
                
                )
        except Exception: # Captura exceções como token_not_valid
            return Response(
            {"detail": "Token inválido."},
            status=status.HTTP_400_BAD_REQUEST
            )
