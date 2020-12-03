class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        print(f"{self.name} {self.surname}")

    def get_total_income(self):
        print(f"Доход с учетом премии равен {self._income.get('wage') + self._income.get('bonus')} руб.")


a = Position("Иван", "Петров", "CEO", 500000, 250000)
a.get_full_name()
print(a.position)
a.get_total_income()
