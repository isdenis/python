class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f"{self.title}. Запуск автоотрисовки.")


class Pen(Stationery):
    def draw(self):
        print(f"{self.title}. Сейчас рисуем ручкой.")


class Pencil(Stationery):
    def draw(self):
        print(f"{self.title}. Сейчас рисуем карандашом")


class Handle(Stationery):
    def draw(self):
        print(f"{self.title}. Сейчас рисуем маркером")


paper = Stationery("Автохудожник")
paper.draw()
paper_pen = Pen("Художник ручкой")
paper_pen.draw()
paper_pencil = Pencil("Художник карандашом")
paper_pencil.draw()
paper_handle = Handle("Художник маркером")
paper_handle.draw()
