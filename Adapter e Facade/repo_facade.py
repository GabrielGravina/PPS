class Update:
    def update_client_profile(self, clientes, cliente_id, novos_dados):
        for cliente in clientes:
            if cliente["id"] == cliente_id:
                cliente.update(novos_dados)
                return "Perfil do cliente atualizado com sucesso"
        return "Cliente não encontrado"

class Recovery:
    def recovery_client(self, clientes, cliente_id):
        for cliente in clientes:
            if cliente["id"] == cliente_id:
                return cliente
        return None
class Cadastro:
    def cadastro_cliente(self, clientes, cliente):
        clientes.append(cliente)
        return "Cliente cadastrado com sucesso"

class Delete:
    def delete_client(self, clientes, cliente_id):
        for cliente in clientes:
            if cliente["id"] == cliente_id:
                clientes.remove(cliente)
                return "Cliente excluído com sucesso"
        return "Cliente não encontrado"

class Facade:
    def __init__(self):
        self.clientes = [] 
        self.cadastro_instancia = Cadastro()
        self.update_instancia = Update()
        self.delete_instancia = Delete()
        self.recovery_instancia = Recovery()

    def cadastro(self, cliente):
        return self.cadastro_instancia.cadastro_cliente(self.clientes, cliente)

    def update(self, cliente_id, novos_dados):
        return self.update_instancia.update_client_profile(self.clientes, cliente_id, novos_dados)

    def delete(self, cliente_id):
        return self.delete_instancia.delete_client(self.clientes, cliente_id)

    def recovery(self, cliente_id):
        return self.recovery_instancia.recovery_client(self.clientes, cliente_id)

repo = Facade()
print(repo.cadastro({'id': 1, 'nome': 'Lucas'}))
print(repo.update(1, {'nome': 'Lucas Silva'}))
print(repo.recovery(1))
print(repo.delete(1))
