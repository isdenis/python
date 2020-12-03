class Car:
    def __init__(self, speed, color, name, is_police="Не полиция"):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print(f"Ваша машина называется {self.name}, у нее цвет {self.color}. {self.is_police}!")

    def go(self):
        print("Она завелась, яяяххуууу!!!!")

    def stop(self):
        print("Ну вот, опять заглохла :(")

    def turn(self, direction):
        print(f"Поворачиваем на {direction}.")

    def show_speed(self):
        print(f"Текущая скорость {self.speed}")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"Ты превысил скорость на {self.speed - 60} км/час, остановись!")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"Ты превысил скорость на {self.speed - 40} км/час, остановись!")


class PoliceCar(Car):
    pass


print("*" * 50)

first_car = Car(180, "красный", "Жигуль")
first_car.go()
first_car.stop()
first_car.turn("лево")
first_car.show_speed()

print("*" * 50)

second_car = TownCar(100, "зеленый", "Феррари")
second_car.go()
second_car.stop()
second_car.turn("право")
second_car.show_speed()

print("*" * 50)

sport_car = SportCar(250, "черный", "Бэнтли")
sport_car.go()
sport_car.stop()
sport_car.turn("лево")
sport_car.show_speed()

print("*" * 50)

work_car = WorkCar(75, "черный", "Ауди")
work_car.go()
work_car.stop()
work_car.turn("лево")
work_car.show_speed()

print("*" * 50)

police_car = PoliceCar(250, "зеленый", "Феррари", "Да, мы из полиции")
police_car.go()
police_car.stop()
police_car.turn("право, лево, право, лево")
police_car.show_speed()

print("*" * 50)
