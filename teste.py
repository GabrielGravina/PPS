class Cafe:
    def __init__(self):
        self.ingredientes = []

    def prepare(self):
        print("Preparando café básico...")
        for ingrediente in self.ingredientes:
            print(f"  - Adicionando {ingrediente}")
        print("Pronto! Uma xícara de café delicioso.")

    def add_ingrediente(self, ingrediente):
        self.ingredientes.append(ingrediente)

class LeiteDecorator(Cafe):
    def __init__(self, cafe):
        super().__init__()
        self.cafe = cafe

    def prepare(self):
        self.cafe.prepare()
        print("  - Adicionando leite")

class AcucarDecorator(Cafe):
    def __init__(self, cafe):
        super().__init__()
        self.cafe = cafe

    def prepare(self):
        self.cafe.prepare()
        print("  - Adicionando açúcar")

class ChocolateDecorator(Cafe):
    def __init__(self, cafe):
        super().__init__()
        self.cafe = cafe

    def prepare(self):
        self.cafe.prepare()
        print("  - Adicionando chocolate")

class ChantillyDecorator(Cafe):
    def __init__(self, cafe):
        super().__init__()
        self.cafe = cafe

    def prepare(self):
        self.cafe.prepare()
        print("  - Adicionando chantilly")

# Café básico
cafe = Cafe()
cafe.prepare()

# Café com leite
cafe_com_leite = LeiteDecorator(cafe)
cafe_com_leite.prepare()

# Café com leite e açúcar
cafe_com_leite_e_acucar = AcucarDecorator(cafe_com_leite)
cafe_com_leite_e_acucar.prepare()

# Café com leite, açúcar e chocolate
cafe_completo = ChocolateDecorator(cafe_com_leite_e_acucar)
cafe_completo.prepare()

# Café com todos os ingredientes
cafe_mega = ChantillyDecorator(cafe_completo)
cafe_mega.prepare()