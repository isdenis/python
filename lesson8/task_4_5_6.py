class Warehouse:
    storage_max = 300  # количество мест хранения

    def __init__(self):
        self.map = {Printer("hn45", "HP", "laser"): 1, Scanner("qy9", "Canon", "A4"): 2,
                    Copier("COP90", "Epson", "color"): 5}
        self.storage_current = Warehouse.storage_max - 1 - 2 - 5

    def __str__(self):
        return f"На складе сейчас {self.map.items()}"

    def add_warehouse(self, office_equipment, count):
        if self.storage_current - count < 0:
            print("нельзя")
        if office_equipment in self.map.keys():
            self.map[office_equipment] = self.map.get(office_equipment) + count
            self.storage_current = self.storage_current - count
            print(self.map.items())
        else:
            self.map[office_equipment] = count
            self.storage_current = self.storage_current - count
            print(self.map.items())
        print(self.storage_current)

    def del_warehouse(self, office_equipment, count):
        if office_equipment in self.map.keys() and self.map.get(office_equipment) > count:
            self.map[office_equipment] = self.map.get(office_equipment) - count
            self.storage_current = self.storage_current + count
            print(self.map.items())
        if office_equipment in self.map.keys() and self.map.get(office_equipment) == count:
            self.map.pop(office_equipment)
            self.storage_current = self.storage_current + count
            print(self.map.items())
        else:
            print("нельзя")

    def remains(self):
        print(f"{'*' * 100}\nНа складе осталось {self.storage_current} местa "
              f"из {Warehouse.storage_max}\n{'*' * 100}")


class OfficeEquipment:
    def __init__(self, name, firm):
        self.name = name
        self.firm = firm

    def __repr__(self):
        return f"{self.name}, {self.firm}"


class Printer(OfficeEquipment):
    def __init__(self, name, firm, type_printer):
        super().__init__(name, firm)
        self.type_printer = type_printer

    def __repr__(self):
        return f"{super().__repr__()}, {self.type_printer}"

    def __eq__(self, other):
        if self.name == other.name and self.firm == other.firm and self.type_printer == other.type_printer:
            return True
        else:
            return False

    def __hash__(self):
        return hash(self.name) + hash(self.firm) + hash(self.type_printer)


class Scanner(OfficeEquipment):
    def __init__(self, name, firm, format_scanner):
        super().__init__(name, firm)
        self.format_scanner = format_scanner

    def __repr__(self):
        return f"{super().__repr__()}, {self.format_scanner}"

    def __eq__(self, other):
        if self.name == other.name and self.firm == other.firm and self.format_scanner == other.format_scanner:
            return True
        else:
            return False

    def __hash__(self):
        return hash(self.name) + hash(self.firm) + hash(self.format_scanner)


class Copier(OfficeEquipment):
    def __init__(self, name, firm, is_color):
        super().__init__(name, firm)
        self.is_color = is_color

    def __repr__(self):
        return f"{super().__repr__()}, {self.is_color}"

    def __eq__(self, other):
        if self.name == other.name and self.firm == other.firm and self.is_color == other.is_color:
            return True
        else:
            return False

    def __hash__(self):
        return hash(self.name) + hash(self.firm) + hash(self.is_color)


what_to_do = int(input("Укажите, что вы ходите сделать?\n1 - добавить технику на склад\n2 - забрать технику со склада"
                       "\nСделайте ваш выбор:  "))
warehouse = Warehouse()
if what_to_do == 1:
    warehouse.remains()
    choise = int(input("Что нужно добавить?\n1 - принтер; 2 - сканер; 3 - копир.\nСделайте ваш выбор: "))
    if choise == 1:
        printer = Printer(input("Введите название: "), input("Введите фирму: "), input("Введите тип: "))
        warehouse.add_warehouse(printer, int(input("Введите количество: ")))
    if choise == 2:
        scanner = Scanner(input("Введите название: "), input("Введите фирму: "), input("Введите формат: "))
        warehouse.add_warehouse(scanner, int(input("Введите количество: ")))
    if choise == 3:
        copier = Copier(input("Введите название: "), input("Введите фирму: "), input("Введите тип: "))
        warehouse.add_warehouse(copier, int(input("Введите количество: ")))

if what_to_do == 2:
    choise = int(input("Что нужно взять?\n1 - принтер; 2 - сканер; 3 - копир.\nСделайте ваш выбор: "))
    if choise == 1:
        printer = Printer(input("Введите название: "), input("Введите фирму: "), input("Введите тип: "))
        warehouse.del_warehouse(printer, int(input("Введите количество: ")))
    if choise == 2:
        scanner = Scanner(input("Введите название: "), input("Введите фирму: "), input("Введите формат: "))
        warehouse.del_warehouse(scanner, int(input("Введите количество: ")))
    if choise == 3:
        copier = Copier(input("Введите название: "), input("Введите фирму: "), input("Введите тип: "))
        warehouse.del_warehouse(copier, int(input("Введите количество: ")))
