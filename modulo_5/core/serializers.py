from rest_framework import serializers
from django.utils.timezone import now
from .models import Tarefa

class TarefaSerializer(serializers.ModelSerializer):
    # Customizar mensagens padrão
    titulo = serializers.CharField(
        max_length=200,
        error_messages={
            'required': 'O título é obrigatório.',
            'blank': 'O título não pode ser vazio.',
            'max_length': 'O título não pode ter mais de 200 caracteres.'
        }
    )

    class Meta:
        model = Tarefa
        fields = ['id', 'user', 'titulo', 'concluida', 'criada_em', 'prioridade', 'prazo']
        read_only_fields = ['id', 'criada_em']
       
    def validate_titulo(self, value):
        """
        Validação customizada para o campo 'titulo'.

        Regras:
        - Não pode ser vazio (após strip)
        - Não pode conter apenas números
        - Deve ter pelo menos 3 caracteres
        """
        # Remover espaços em branco
        value = value.strip()
        # Validação 1: Não vazio
     
            
        if not value:
            raise serializers.ValidationError(
                "O título não pode ser vazio ou conter apenas espaços."
            )
        # Validação 2: Mínimo de caracteres
        if len(value) < 3:
            raise serializers.ValidationError(
            "O título deve ter pelo menos 3 caracteres."
            )
        # Validação 3: Não apenas números
        if value.isdigit():
            raise serializers.ValidationError(
                "O título não pode conter apenas números."
            )
        
        user = self.context['request'].user

        if Tarefa.objects.filter(user=user, titulo=value).exists():
            raise serializers.ValidationError(
                "Você já tem uma tarefa com este título."
            )

        return value

    def validate_prioridade(self, value):

        value = value.strip().lower()
        valores_validos = ["baixa", "media", "alta"]

        if value.isdigit():
            raise serializers.ValidationError(
                "Prioridade não pode ser números. use: baixa, media ou alta"
            )
        
        if value not in valores_validos:
            raise serializers.ValidationError(
                "prioridade só aceita valores como: baixa, media ou alta "
            )
        return value
        
    def validate_prazo(self, value):

        if value and value < now().date():
            raise serializers.ValidationError(
                "O prazo não pode ser no passado."
            )
        return value

    def validate(self, data):
        concluida = data.get('concluida', False)
        prazo = data.get('prazo')
       
        if not concluida and not prazo:
                raise serializers.ValidationError({
                    'prazo': 'O prazo é obrigatório para tarefas não concluídas.'
                })

        return data