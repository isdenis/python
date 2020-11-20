# сделал в одной задаче и list и dict. List месяц у меня, dict - времена года.

month_digit = int(input("Введите номер месяца цифрой от 1 до 12: "))
month_list = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь',
              'ноябрь', 'декабрь']
month_dict = {1: 'зима', 2: 'весна', 3: 'лето', 4: 'осень'}

while month_digit not in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12):
    print("Нет такого месяца, попробуйте еще.")
    month_digit = int(input("Введите номер месяца цифрой от 1 до 12: "))

month_for_dict = month_digit
if month_for_dict in (12, 1, 2):
    month_for_dict = 1
elif month_for_dict in (3, 4, 5):
    month_for_dict = 2
elif month_for_dict in (6, 7, 8):
    month_for_dict = 3
elif month_for_dict in (9, 10, 11):
    month_for_dict = 4

print(f"Месяц, который вы выбрали - {month_list[month_digit - 1]}. "
      f"Соответственно, это {month_dict.get(month_for_dict)}.")
