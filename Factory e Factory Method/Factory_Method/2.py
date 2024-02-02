from abc import ABC

class Enemy(ABC):
    def attack(self):
        pass

class Fantasma(Enemy):
    def attack(self):
        print("O fantasma está atacando")

class Boss(Enemy):
    def attack(self):
        print("O chefão está atacando")

class EnemyFactory:
    def create_enemy(self, level):
        if level == 1:
            return Fantasma()
        elif level == 2:
            return Boss()
        else:
            raise ValueError(f"Nível de inimigo inválido: {level}")

class InstanceOfGame:
    def __init__(self, level):
        self.level = level
        self.factory = EnemyFactory()
        self.enemy = self.factory.create_enemy(self.level)

    def play_game(self):
        print(f"Inimigo do nível {self.level}:")
        self.enemy.attack()

if __name__ == "__main__":
    game_instance = InstanceOfGame(level=2)
    game_instance.play_game()
