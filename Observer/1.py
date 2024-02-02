class ClickTracker:
    def __init__(self):
        self.clicks_num = 0
        self.observers = []

    def increase_clicks(self):
        self.clicks_num += 1
        self.notify_observers()

    def add_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.clicks_updated(self.clicks_num)
    def kill_observer(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

class ClickObserver:
    def clicks_updated(self, new_clicks_num):
        print(f"O número de cliques foi atualizado para {new_clicks_num}.")

if __name__ == "__main__":
    click_tracker = ClickTracker()
    click_observer = ClickObserver()
    click_tracker.add_observer(click_observer)

    click_tracker.increase_clicks()
    click_tracker.increase_clicks()
    click_tracker.increase_clicks()


    #Obs.: após remover o observador criado, o código não mostrará mais a mensagem caso atualize a quantidade de clicks
    click_tracker.kill_observer(click_observer)
    click_tracker.increase_clicks()
