import random

class Mensagem:
    def __init__(self, remetente, conteudo):
        self.remetente = remetente
        self.conteudo = conteudo

class Chat:
    def __init__(self):
        self.mensagens = []
        self.clientes = []

    def enviar_mensagem(self, remetente, conteudo):
        nova_mensagem = Mensagem(remetente, conteudo)
        self.mensagens.append(nova_mensagem)
        self.notificar_clientes(nova_mensagem)

    def notificar_clientes(self, nova_mensagem):
        for cliente in self.clientes:
            if cliente != nova_mensagem.remetente:
                cliente.receber_notificacao(nova_mensagem)

class Cliente:
    def __init__(self, nome, chat):
        self.nome = nome
        self.chat = chat
        self.chat.clientes.append(self)

    def enviar_mensagem(self, conteudo):
        self.chat.enviar_mensagem(self, conteudo)

    def receber_notificacao(self, nova_mensagem):
        print(f"\nNotificação para {self.nome}: Nova mensagem de {nova_mensagem.remetente.nome}: {nova_mensagem.conteudo}")


chat = Chat()

pedro = Cliente("Pedro", chat)
marcela = Cliente("Marcela", chat)
lucas = Cliente("Lucas", chat)

pedro.enviar_mensagem("Oi, pessoal!")
marcela.enviar_mensagem("Oi, Pedro!")
lucas.enviar_mensagem("E aí, galera?")
