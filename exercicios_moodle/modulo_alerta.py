class Usuario:
    def __init__(self,nome, email):
        self.nome = nome
        self.__email = email

    @property
    def email(self) -> str:
        return self.__email
    
    @email.setter
    def email(self, novo_email: str) -> None:
        if '@' not in novo_email:
            raise ValueError("Erro: O email deve conter o caractere: '@' ")
        self.__email = novo_email

class CanalEnvio():

    def enviar(self) -> None:
        raise NotImplementedError("implemente sua propia Lógica")
    
class Email(CanalEnvio):
    
    def enviar(self, mensagem) -> str:
        return f"📧 Enviando para servidor de email: [{mensagem}]"

class SMS(CanalEnvio):
    
    def enviar(self, mensagem) -> str:
        return f"� Enviando para operadora telefônica: [{mensagem}]"

class SistemaAlerta:

    def __init__(self,usuario, canal):
        self.usuario = usuario
        self.canal = canal
    
    def disparar_texto(self, mensagem):
        nome_usuario = self.usuario.nome
        resultado = self.canal.enviar(f"{nome_usuario}: {mensagem}")
        print(resultado)
        return resultado

print("TESTE 1: SEGURANÇA - VALIDAÇÃO DE EMAIL")


usuario = Usuario("Thiago", "thiago@email.com")
print(f"Usuário criado: {usuario.nome} | Email: {usuario.email}")


print("\nTentando mudar para email INVÁLIDO sem '@'")

try:
    usuario.email = "emailinvalido.com"
    print("FALHA: Sistema permitiu email inválido!")
except ValueError as e:
    print(f"BLOQUEADO: {e}")
    print(f"Email mantido: {usuario.email}")

print("\n Mudando para email VÁLIDO...")
try:
    usuario.email = "thiago.novo@gmail.com"
    print(f"SUCESSO: Email atualizado para {usuario.email}")
except ValueError as e:
    print(f"ERRO: {e}")

print("TESTE 2: ENVIO POR EMAIL")


canal_email = Email()
print("\n Canal de Email instanciado")


sistema_email = SistemaAlerta(usuario, canal_email)
print(f"Sistema de Alerta criado com usuário '{usuario.nome}' e canal Email")

print("\nDisparando mensagem por Email...")
sistema_email.disparar_texto("Alerta de segurança no sistema!")


print("TESTE 3: POLIMORFISMO - TROCA DE CANAL PARA SMS")

canal_sms = SMS()
print("\nCanal de SMS instanciado")

sistema_sms = SistemaAlerta(usuario, canal_sms)
print(f"Novo Sistema de Alerta criado com o MESMO usuário '{usuario.nome}' e canal SMS")

print("\nDisparando mensagem por SMS...")
sistema_sms.disparar_texto("Código de verificação: 123456")

