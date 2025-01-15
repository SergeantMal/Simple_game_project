# Программа простой игры, реализующая бой игрока с монстром с возможностью выбора оружия.
# В программе используется один из основных принципов SOLIP - OCP (Open/Closed Principle).

from abc import ABC, abstractmethod
import random


# Абстрактный класс оружия

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

# Классы оружия

class Sword(Weapon):
    def __init__(self):
        self.name = "Меч"

    def attack(self): # Метод атаки
        print("Игрок наносит удар мечом")
        return random.randint(20, 30)

class Bow(Weapon):
    def __init__(self):
        self.name = "Лук"

    def attack(self):   # Метод атаки
        print("Игрок стреляет из лука")
        return random.randint(10, 30)

class Axe(Weapon):
    def __init__(self):
        self.name = "Топор"

    def attack(self):   #
        print("Игрок наносит удар топором")
        return random.randint(15, 30)

class Monster():
    def __init__(self, hp):
        self.hp = hp
    def attack(self): #Метод атаки
        monster.hp -= random.randint(1, 30)
        print("Монстр наносит удар")

# Класс игрока

class Fighter():
    def __init__(self, hp, weapon):
        self.weapon = weapon
        self.hp = hp

    def change_weapon(self, weapon): # Метод смены оружия
        self.weapon = weapon
        print(f"Игрок сменил оружие на {self.weapon.name}")

# Метод смены оружия

def change_weapon(fighter: Fighter):
    while True:
        choice = input("Выберите оружие: 1 - меч, 2 - лук, 3 - топор ")
        if choice == '1':
            fighter.change_weapon(Sword())
            break
        elif choice == '2':
            fighter.change_weapon(Bow())
            break
        elif choice == '3':
            fighter.change_weapon(Axe())
            break
        else:
            print("Неправильная команда")


# Метод боя

def fight(fighter: Fighter, monster: Monster):
    change_weapon(fighter)
    while fighter.hp > 0 and monster.hp > 0:
        fighter.hp -= fighter.weapon.attack()
        monster.attack()
        print(f"У игрока осталось {fighter.hp} здоровья")
        print(f"У монстра осталось {monster.hp} здоровья")
        if fighter.hp <= 0 or monster.hp <= 0:
            break
        if input("Хотите сменить оружие? (y/n)") == 'y':
            change_weapon(fighter)
        else:
            pass

    if fighter.hp > 0:
        print("Победил игрок")
    else:
        print("Победил монстр")

# Создание игрока и монстра

figher = Fighter(random.randint(50, 100), Sword())
monster = Monster(random.randint(50, 100))

# Бой

fight(figher, monster)
