from abc import ABC

class Observer(ABC):
    def update(self, product, price):
        pass

class Subject(ABC):
    def add_observer(self, observer):
        pass

    def remove_observer(self, observer):
        pass

    def notify_observers(self, product, price):
        pass

class PriceTracker(Subject):
    def __init__(self):
        self._observers = []
        self._product_prices = {}

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, product, price):
        for observer in self._observers:
            observer.update(product, price)

    def set_price(self, product, price):
        if product in self._product_prices and self._product_prices[product] > price:
            self.notify_observers(product, price)
        self._product_prices[product] = price

class Customer(Observer):
    def __init__(self, name):
        self._name = name

    def update(self, product, price):
        print(f"{self._name} - Price update for {product}: R${price:.2f}")

if __name__ == "__main__":
    tracker = PriceTracker()

    customer1 = Customer("Customer A")
    customer2 = Customer("Customer B")

    tracker.add_observer(customer1)
    tracker.add_observer(customer2)

    tracker.set_price("Product X", 19.90)
    tracker.set_price("Product Y", 29.99)
    print("---- Product X price alteration -----")
    tracker.set_price("Product X", 17.99)
    tracker.set_price("Product X", 23.95)
    tracker.set_price("Product X", 19.90)



#Coloquei pra fazer com que só notifique os preços caso haja uma promoção. Ele só irá printar caso o novo preço
# seja menor que o preço anterior