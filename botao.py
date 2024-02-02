class Botao:
    def __init__(self):
        pass

    def render(self):
        print("Renderizando botão básico...")

class DecoratorBotao(Botao):
    def __init__(self, botao):
        super().__init__()
        self.botao = botao

    def render(self):
        self.botao.render()

class BordaSimplesDecorator(DecoratorBotao):
    def render(self):
        super().render()
        print("  - Adicionando borda simples")

class BordaDuplaDecorator(DecoratorBotao):
    def render(self):
        super().render()
        print("  - Adicionando borda dupla")

class BordaTracejadaDecorator(DecoratorBotao):
    def render(self):
        super().render()
        print("  - Adicionando borda tracejada")

class Formulario:
    def __init__(self):
        self.campos = []

    def render(self):
        print("Renderizando formulário básico...")
        for campo in self.campos:
            campo.render()

    def add_campo(self, campo):
        self.campos.append(campo)


class DecoratorFormulario(Formulario):
    def __init__(self, formulario):
        super().__init__()
        self.formulario = formulario

    def render(self):
        self.formulario.render()


class CampoTextoDecorator(DecoratorFormulario):
    def render(self):
        super().render()
        print("  - Adicionando campo de texto")


class CampoSelecaoDecorator(DecoratorFormulario):
    def render(self):
        super().render()
        print("  - Adicionando campo de seleção")


class CampoDataDecorator(DecoratorFormulario):
    def render(self):
        super().render()
        print("  - Adicionando campo de data")


# Exemplo de uso
botao = Botao()
botao_decorado = BordaSimplesDecorator(botao)
botao_decorado.render()

formulario = Formulario()
formulario_decorado = CampoTextoDecorator(formulario)
formulario_decorado.add_campo(CampoSelecaoDecorator(formulario_decorado))
formulario_decorado.add_campo(CampoDataDecorator(formulario_decorado))
formulario_decorado.render()
