class Road:
    weight = 25
    thickness = 5

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculation(self):
        print(f"Асфальта нужно: {self._length * self._width * Road.weight * Road.thickness / 1000} тонны")


a = Road(25, 8000)
a.calculation()
