import random

class Noticia:
    def __init__(self, headline, text):
        self.headline = headline
        self.text = text

noticia1 = Noticia("Operação da PF apreende equipamentos de garimpeiros que voltaram para Terra Yanomami",
                   "Ação é parte das medidas para retirar invasores que permanecem no território ou que voltaram depois das ações de 2023. Foram apreendidos armas, radiocomunicadores, munição e coletes à prova de bala.")

noticia2 = Noticia("Enem 2023: O que dizem os alunos que tiraram nota mil na redação",
                   "Segundo Inep, 60 estudantes atingiram nota máxima na redação do Enem em 2023; g1 reúne histórias de quem conseguiu essa pontuação.")

noticia3 = Noticia("Com queda de quase 3 milhões, população da China encolhe pelo segundo ano seguido",
                   "Entre as razões para a redução populacional está a queda na taxa de natalidade e a onda de mortes provocadas pela Covid-19. Número de habitantes está em 1,4 bilhão.")

class NewsTracker:
    def __init__(self, *noticias):
        self.noticias_disponiveis = list(noticias)
        self.noticia_atual = random.choice(self.noticias_disponiveis)
        self.observers = []

    def alt_noticia_aleatoria(self):
        nova_noticia = random.choice(self.noticias_disponiveis)
        self.noticia_atual = nova_noticia
        self.notify_observers()

    def add_observer(self, observer):
        self.observers.append(observer)

    def kill_observer(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.noticia_atualizada(self.noticia_atual)

class NewsObservable:
    def __init__(self, name):
        self.name = name

    def noticia_atualizada(self, nova_noticia):
        print(f"\nNotícia enviada para {self.name}: {nova_noticia.headline}\n{nova_noticia.text}")

if __name__ == "__main__":
    news_tracker = NewsTracker(noticia1, noticia2, noticia3)

    while True:
        print("\nOpções:")
        print("1. Adicionar Observer")
        print("2. Remover Observer")
        print("3. Gerar Notícia Aleatória")
        print("4. Sair")

        choice = input("Escolha uma opção: ")

        if choice == "1":
            name = input("Digite o nome do Observer a ser adicionado: ")
            news_observer = NewsObservable(name)
            news_tracker.add_observer(news_observer)
            print(f"Observer {name} adicionado com sucesso.")
        elif choice == "2":
            name = input("Digite o nome do Observer a ser removido: ")
            temp_observer = next((observer for observer in news_tracker.observers if observer.name == name), None)
            if temp_observer:
                news_tracker.kill_observer(temp_observer)
                print(f"Observer {name} removido com sucesso.")
            else:
                print(f"Observer {name} não encontrado.")
        elif choice == "3":
            news_tracker.alt_noticia_aleatoria()
            print("Notícia gerada e enviada para Observers.")
        elif choice == "4":
            break
        else:
            print("Opção inválida. Tente novamente.")
