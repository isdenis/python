class Cells:
    def __init__(self, cells_sum):
        self.cells_sum = cells_sum

    def __add__(self, other):  # сложение
        return self.cells_sum + other.cells_sum

    def __sub__(self, other):  # вычитание
        return self.cells_sum - other.cells_sum if (self.cells_sum - other.cells_sum) > 0 \
            else f"разность количества ячеек двух клеток не может быть меньше нуля, а сейчас получается " \
                 f"{self.cells_sum - other.cells_sum}."

    def __mul__(self, other):  # умножение
        return self.cells_sum * other.cells_sum

    def __floordiv__(self, other):  # деление
        return self.cells_sum // other.cells_sum

    def make_order(self, raw):
        return "\n".join("*" * raw for i in range(self.cells_sum // raw)) + "\n" + "*" * (self.cells_sum % raw)


cell_1 = Cells(11)
cell_2 = Cells(15)

print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 // cell_2)
print(cell_1.make_order(8))
