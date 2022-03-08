class Car:

    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        print(f'автомобиль {self.name} поехал со скоростью {self.speed} км/ч')

    def stop(self):
        print(f'автомобиль {self.name} остановился')

    def turn(self, direction):
        print(f'автомобиль {self.name} повернул {direction}')

    def show_speed(self):
        print(f'текущая скорость автомобиля {self.name} составляет {self.speed} км/ч')


class TownCar(Car):
    def show_speed(self):
        speed = 60
        if self.speed > speed:
            print(f'Скорость превышена на {self.speed - speed} км/ч')


class WorkCar(Car):
    def show_speed(self):
        speed = 40
        if self.speed > speed:
            print(f'Скорость превышена на {self.speed - speed} км/ч')


class SportCar(Car):
    pass


class PoliceCar(Car):
    pass


police = PoliceCar('Mazda', "blue", 70, is_police=True)
police.show_speed()
my_car = TownCar('Audi', 'black', 80)
driver = WorkCar('Ford', 'red', 50)
my_car.show_speed()
driver.show_speed()
driver.turn('left')
my_car.go()
