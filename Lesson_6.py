# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.

class TownCar:
    def __init__(self, speed, color, name, is_police):
        self._speed = speed
        self._name = name
        self._is_police = bool(is_police)
        self._color = color

    def go(self):
        print('Going')

    def stop(self):
        print('Stoping')

    def turn(self, turn):
        print('Turning to the ' + turn)


class SportCar(TownCar):
    def __init__(self, speed, color, name, is_police):
        TownCar.__init__(self, speed, color, name, is_police)



class WorkCar(TownCar):
    def __init__(self, speed, color, name, is_police):
        TownCar.__init__(self, speed, color, name, is_police)
    
    
class PoliceCar(TownCar):
    def __init__(self, speed, color, name, is_police):
        TownCar.__init__(self, speed, color, name, is_police)

car = SportCar('20','red', 'racer', False)
print(car._is_police)
car.go()
car.turn('left')


# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.

class person:

    def __init__(self, name, health, armor, damage):
        self.name = name
        self.health = health
        self.armor = armor
        self.damage = damage

    def _calculateDamage(self, player):
        return self.damage / player.armor

    def attack(self, player):
        player.health -= self._calculateDamage(enemy)


class player(person):
    pass


class enemy(person):
    pass


class game:

    def __init__(self, player, enemy):
        self._player = player
        self._enemy = enemy

    def start(self):
        last_attacker = self._player
        while self._player.health > 0 and self._enemy.health > 0:
            if last_attacker == self._player:
                self._enemy.attack(self._player)
                last_attacker = self._enemy
            else:
                self._player.attack(self._enemy)
                last_attacker = self._player
        if player.health > 0:
            print('player win')
        else:
            print('enemy win')


player = player('Player', 100, 1.1, 30)
enemy = enemy('Enemy', 100, 1.2, 10)
game = game(player, enemy)

game.start()


# Задача - 1
# Вам необходимо создать завод по производству мягких игрушек для детей.
# Вам надо продумать структуру классов,
# чтобы у вас был класс, который создает игрушки на основании:
#  Названия, Цвета, Типа (животное, персонаж мультфильма)
# Опишите процедуры создания игрушки в трех методах:
# -- Закупка сырья, пошив, окраска
# Не усложняйте пусть методы просто выводят текст о том, что делают.
# В итоге ваш класс по производству игрушек должен вернуть объект нового класса Игрушка.

class toy:

    def __init__(self, name, color):
        self.name = name
        self.color = color


class animal(toy):

    def __init__(self, name, color):
        toy.__init__(self, name, color)
        self.type = 'Животное'


class cartoon(toy):

    def __init__(self, name, color):
        toy.__init__(self, name, color)
        self.type = 'Мультфильм'


class fabrick:

    def CreateToy(self, name, color, toy_type):
        self._buying()
        self._sewing()
        self._painting()

        if toy_type == 'животное':
            return animal(name, color)
        elif toy_type == 'мультфильм':
            return cartoon(name, color)

    def _buying(self):
        print('Buying materials')

    def _sewing(self):
        print('Sweing toy')

    def _painting(self):
        print('Painting toy')



factory = fabrick()
toy = factory.CreateToy('Lion', 'orange', 'животное')
