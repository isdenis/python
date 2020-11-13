print("Сейчас необходимо будет ввести значения выручки и издержек фирмы.")
revenue = int(input("Введите выручку: "))
expenses = int(input("Введите издержки: "))
profit = revenue - expenses
if profit > 0:
    print(f"У вас прибыльная фирма. Прибыль составила {profit} руб.")
    rent = (revenue - expenses) / revenue
    print(f"Рентабельность фирмы составила {round(rent,2)} %")
    sotr = int(input("Введите количество ваших сотрудников: "))
    print(f"Прибыль фирмы на одного сотрудника составляет {profit / sotr} руб.")
if profit < 0:
    print(f"У вас убыточная фирма. Убыток составил {profit} руб.")