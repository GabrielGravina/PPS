from abc import ABC, abstractmethod

class Burger(ABC):
    def get_description(self):
        pass

    def get_cost(self):
        pass

class BasicBurger(Burger):
    def get_description(self):
        return "Basic Burger"

    def get_cost(self):
        return 12.0

class BurgerDecorator(Burger, ABC):
    def __init__(self, burger):
        self._burger = burger

    def get_description(self):
        return self._burger.get_description()

    def get_cost(self):
        return self._burger.get_cost()

class CheeseDecorator(BurgerDecorator):
    def __init__(self, burger):
        super().__init__(burger)

    def get_description(self):
        return super().get_description() + ", Cheese"

    def get_cost(self):
        return super().get_cost() + 1.5

class BaconDecorator(BurgerDecorator):
    def __init__(self, burger):
        self._burger = burger

    def get_description(self):
        return super().get_description() + ", Bacon"

    def get_cost(self):
        return super().get_cost() + 2.0

if __name__ == "__main__":
    basic_burger = BasicBurger()
    print(f"Description: {basic_burger.get_description()}, Cost: R${basic_burger.get_cost()}")

    cheese_burger = CheeseDecorator(basic_burger)
    print(f"Description: {cheese_burger.get_description()}, Cost: R${cheese_burger.get_cost()}")

    bacon_cheese_burger = BaconDecorator(cheese_burger)
    print(f"Description: {bacon_cheese_burger.get_description()}, Cost: R${bacon_cheese_burger.get_cost()}")
