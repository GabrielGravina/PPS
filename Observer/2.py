import random
class TempTracker:
    def __init__(self):
        self.tempC = 25
        self.observers = []

    def alt_temp(self):
        def gerar_numero_aleatorio():
            return random.randint(-5, 5)
        tempIncrease = gerar_numero_aleatorio()
        print(tempIncrease)
        self.tempC = self.tempC + tempIncrease
        self.notify_observers()

    def add_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.clicks_updated(self.tempC)

class TempObserver:
    def clicks_updated(self, new_tempC):
        print(f"Temperatura atual: {new_tempC}.")

if __name__ == "__main__":
    temp_tracker = TempTracker()
    click_observer = TempObserver()
    temp_tracker.add_observer(click_observer)

    temp_tracker.alt_temp()
    temp_tracker.alt_temp()
    temp_tracker.alt_temp()
