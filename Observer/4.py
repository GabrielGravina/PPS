import random

class Produto:
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade

class Estoque:
    def __init__(self, *produtos):
        self.produtos_disponiveis = list(produtos)
        self.produto_atual = random.choice(self.produtos_disponiveis)
        self.observers = []

    def atualizar_quantidade(self, novo_produto, nova_quantidade):
        for produto in self.produtos_disponiveis:
            if produto.nome == novo_produto.nome:
                produto.quantidade = nova_quantidade
                self.produto_atual = produto
                self.notify_observers()

    def add_observer(self, observer):
        self.observers.append(observer)

    def remover_observer(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.produto_atualizado(self.produto_atual)

class EstoqueObservable:
    def __init__(self, name):
        self.name = name

    def produto_atualizado(self, produto):
        print(f"\nNotificação enviada para {self.name}: {produto.nome} - Quantidade: {produto.quantidade}")
        

produto1 = Produto("Laptop", 20)
produto2 = Produto("Smartphone", 50)
produto3 = Produto("Tablet", 30)

estoque = Estoque(produto1, produto2, produto3)
observador1 = EstoqueObservable("Armazém Principal")
observador2 = EstoqueObservable("Loja A")
observador3 = EstoqueObservable("Loja B")

estoque.add_observer(observador1)
estoque.add_observer(observador2)
estoque.add_observer(observador3)

novo_produto = Produto("Laptop", 15)
estoque.atualizar_quantidade(novo_produto, 15)
