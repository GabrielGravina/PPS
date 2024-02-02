class Servico:
    def realizar_servico(self):
        pass

class ServicoExistente:
    def metodo_existente(self):
        print("Método A sendo chamado")

class AdapterServicoExistente(Servico):
    def __init__(self, servico_existente):
        self.servico_existente = servico_existente

    def realizar_servico(self):
        print("Adapter chamando método A através da nova interface")
        self.servico_existente.metodo_existente()

class Cliente:
    def __init__(self, servico):
        self.servico = servico

    def requisitar_servico(self):
        print("Cliente requisitando serviço")
        self.servico.realizar_servico()

if __name__ == "__main__":
    servico_existente = ServicoExistente()
    adapter_servico_existente = AdapterServicoExistente(servico_existente)
    cliente = Cliente(adapter_servico_existente)
    cliente.requisitar_servico()
