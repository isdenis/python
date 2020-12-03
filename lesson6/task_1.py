import time


class TrafficLight:
    __color = ["Красный", "Желтый", "Зеленый"]

    def running(self):
        while True:
            if TrafficLight.__color[0] == "Красный":
                print(TrafficLight.__color[0])
            else:
                print("Проблема со светофором, его работа завершена")
                break
            time.sleep(7)
            if TrafficLight.__color[1] == "Желтый":
                print(TrafficLight.__color[1])
            else:
                print("Проблема со светофором, его работа завершена")
                break
            time.sleep(2)
            if TrafficLight.__color[2] == "Зеленый":
                print(TrafficLight.__color[2])
            else:
                print("Проблема со светофором, его работа завершена")
                break
            time.sleep(5)
            if TrafficLight.__color[1] == "Желтый":
                print(TrafficLight.__color[1])
            else:
                print("Проблема со светофором, его работа завершена")
                break


a_1 = TrafficLight()
a_1.running()
