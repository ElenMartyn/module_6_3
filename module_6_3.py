import random

class Animal:
    live = True
    sound = None # звук
    _DEGREE_OF_DANGER = 0 # степень опасности существа

    def __init__(self, speed):
        self._cords = [0, 0, 0]  # координаты в пространстве
        self.speed = speed  # скорость передвижения

    def move(self, dx, dy, dz): # Изменяем координаты с учетом скорости
        new_z = self._cords[2] + dz * self.speed
        if new_z < 0:
            print("It's too deep, i can't dive :(")
            return
        self._cords[0] += dx * self.speed
        self._cords[1] += dy * self.speed
        self._cords[2] = new_z

    def get_cords(self):
        print(f"X: {self._cords[0]} Y: {self._cords[1]} Z: {self._cords[2]}")

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    def speak(self):
        print(self.sound)


class Bird(Animal):
    beak = True

    def lay_eggs(self):
        eggs = random.randint(1, 4)
        print(f"Here are(is) {eggs} eggs for you")


class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        dz = abs(dz)  # координата z
        self.move(0, 0, -dz)  # скорость при нырянии уменьшается в 2 раза
        self.speed /= 2


class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8


class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):
    sound = "Click-click-click"

    def __init__(self, speed):
        super().__init__(speed)


print('Есть утконос')
db = Duckbill(10)
print('Живой? ', db.live)
print('Клюв есть?:', db.beak)
print('Какой звук издает?')
db.speak()
print('Что делает?')
db.attack()
print('Передвижение утконоса')
db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()
print('Сколько яиц отложил?')
db.lay_eggs()