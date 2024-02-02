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


class DecoratorCafe(Cafe):
    def __init__(self, cafe):
        super().__init__()
        self.cafe = cafe

    def prepare(self):
        self.cafe.prepare()


class LeiteDecorator(DecoratorCafe):
    def prepare(self):
        super().prepare()
        print("  - Adicionando leite")


class AcucarDecorator(DecoratorCafe):
    def prepare(self):
        super().prepare()
        print("  - Adicionando açúcar")


class ChocolateDecorator(DecoratorCafe):
    def prepare(self):
        super().prepare()
        print("  - Adicionando chocolate")


class ChantillyDecorator(DecoratorCafe):
    def prepare(self):
        super().prepare()
        print("  - Adicionando chantilly")


cafe = Cafe()
cafe.prepare()

cafe_com_leite = LeiteDecorator(cafe)
cafe_com_leite.prepare()

cafe_com_leite_e_acucar = AcucarDecorator(cafe_com_leite)
cafe_com_leite_e_acucar.prepare()

cafe_completo = ChocolateDecorator(cafe_com_leite_e_acucar)
cafe_completo.prepare()

cafe_mega = ChantillyDecorator(cafe_completo)
cafe_mega.prepare()
