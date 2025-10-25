# user_service.py
from user_model import UserModel
from hasher import hash_senha, verificar_senha


class UserService:

    def __init__(self):
      self._user_model = UserModel()

    def _safe_user_data(self, user) -> dict | None:
        """
        este é um método privado que recebe um usuarios do banco.
        verifique se o usuários existe e então retorne ele sem a sua senha
        caso ele não exista retorne None
        """
        if not user:
            return None
        else:
            user.pop('senha_hash', None)
            return user

    def _is_authorized(
        self,
        current_user_id: int | None,
        current_user_profile: str,
        target_user_id: int,
        action: str,
    ) -> bool:
        """
        Método que verifica o perfil do usuários, se for Diretoria retorne true
        Se não tiver target_user_id retorn false
        Se  action == "edit_self" retorne current_user_id == target_user_id
        No geral retorn false
        """
        if current_user_profile == 'Diretoria':
            return True
        
        if not target_user_id:
            return False
        
        if action == 'edit_self':
            return current_user_id == target_user_id
    
        return False
    
    def register_user(
        self,
        senha: str,
        email: str,
        nome_completo: str,
        perfil: str = "Afiliado",
    ) -> tuple[bool, str]:
        """
        Método para criar um usuários.
        o campo senha deve ter no mínimo 8 caracteres, caso contrário retorne False a mensagem de erro.
        O campo email deve ter pelo menos 10 caracteres, uma @ e terminar com .com, retorne False se não tiver e a mensagem de erro.
        O campo Nome deve ter apenas letras e não deve estar vazio, retorne False se não tiver e a mensagem de erro.
        Caso os campos atendas as requisições, faça o hash da senha e salve use o método create_user da User Model
        """
       
        if len(senha) < 8:
                return False, 'Error, senha deve ter no minimo 8 carateres' 
            
        if len(email) < 10 or '@' not in email or not email.endswith('.com')  :
                return False, 'Error, Email deve ter no minimo 10 caracteres, ter um @ e terminar com .com'
            
        if not nome_completo.isalpha() and not nome_completo.strip():
            return False, 'Error, apenas letras e não pode estar vazio'
        
        senha_hash = hash_senha(senha)
        return self._user_model.create_user(senha_hash, email, nome_completo, perfil)

    def login_user(self, email: str, senha: str) -> tuple[dict | None, str]:
        """
        Este método é o login do usuários, deve receber um email e senha não vazios
        Use o método do find_user_by_email para buscar o usuario
        Se houver usuarios faça a comparação da senha passada com a senha hash do DB
        Use a função verificar_senha, se tiver ok, retorn o usuarios pelo método privado _safe_user_data
        e a mensagem Login bem-sucedido!.
        Caso contrario retorne None e a mensagem de erro
        """
        if not email.strip() or not senha.strip():
            return None, 'não deixe os campos vazios'
        
        user = self._user_model.find_user_by_email(email)
        
        if not user:
            return None, 'Usuario não encontrado'

        if not verificar_senha(senha, user['senha']):
            return None, 'Senha incorreta'
        
        return self._safe_user_data(user), 'Login bem-sucedido!'
    
    def update_user_profile(
        self,
        current_user_id: int | None,
        current_user_profile: str,
        target_user_id: int,
        new_data: dict,
    ) -> tuple[bool, str]:
        """
        Método para atualizar usuários.
        Chame o método privado _is_authorized, se o retorno for false, retorne false e acesso negado
        Confira as chaves em new_data (senha, nome_completo, email), se pelo menos um desses campos,
        Caso não haja nenhum valor a ser atualizado, encerre a função com False e mensagem de erro.
        Caso contrátio, chame o método da UserModel update_user_by_id passando o id e o new data
        """
        if not self._is_authorized(current_user_id, current_user_profile, target_user_id):
            return False, "Acesso negado"
        
        campos_validos = {'senha', 'nome_completo', 'email'}
        dados_validos = {}
        for i, j in new_data.items():
            if i in campos_validos and j:
                dados_validos[i] = j

        if not dados_validos:
            return False, 'Nenhum dado válido para atualização'

        atualizado = self._user_model.update_user_by_id(target_user_id, dados_validos)

        if atualizado:
            return True, 'Usuario atualizado com sucesso!'
        else:
            return False, 'Erro ao atualizar usuario'

    def delete_user(
        self,
        current_user_profile: str,
        user_id: int,
    ) -> tuple[bool, str]:
        """
        Método para deletar usuarios.
        So é permitido deletar usuarios se o current_user_profile for Diretoria.
        Caso não seja retorn false e a mensagem de acesso negado
        Senão chame o método delete_user_by_id, passando o id do usuários
        """ 
        if not current_user_profile == 'Diretoria':
            return False, 'Acesso Negado'
        deletado = self._user_model.delete_user_by_id(user_id)

        if deletado:
            return True, 'Usuario deletado com sucesso!'
        else:
            return False, 'Erro ao deletar usuario ou usuario não encontrado'
        
    def get_user_by_id(self, user_id: int) -> dict | None:
        """
        Método para pegar um usuarios pelo id
        Retorne o usuarios apos passar pelo método _safe_user_data
        """
        pegando_usuario = self._user_model.find_user_by_id(user_id)
        
        if not pegando_usuario:
            return None
    
        return self._safe_user_data(pegando_usuario)

    def get_all_users(self) -> list[dict | None]:
        """
        Método para retornar todos os usuários.
        retorne todos os usuáriso apos passar pelo método _safe_user_data
        """
        usuarios = self._user_model.get_all_users()
        
        if not usuarios:
            return []
        
        metodo_safe = [self._safe_user_data(usuarios) for usuario in usuarios]
        return metodo_safe