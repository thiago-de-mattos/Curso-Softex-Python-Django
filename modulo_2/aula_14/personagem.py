import random

class Personagem:

    def __init__(self,nome, vida, ataque, pocoes=0):
        self.nome = nome
        self.vida = vida
         



         
        self.ataque = ataque
        self.pocoes =  pocoes
        self.defendendo = False

    def atacar(self, alvo):
        dano = self.ataque
    
        if random.random() < 0.2:
            dano *= 2
            print(f"Ataque Critico de {self.nome}!")
            print(f"{self.nome} ataca {alvo.nome} causando {dano} de dano")
            alvo.receber_dano(dano)

    def dafender(self):
        pass
    def receber_dano(self, dano):

        if self.defendendo:
            dano = dano // 2
            print(f"{self.nome} defendeu e reduziu o dano para {dano}")
            self.defendendo = False
        
        self.vida -= dano
