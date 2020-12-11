# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
# ситуацию и не завершиться с ошибкой.

class OwnError(Exception):
    def __init__(self, err):
        self.err = err


try:
    del_number_1 = int(input("Сейчас будем делить. Введите делимое: "))
    del_number_2 = int(input("Введите делитель: "))
    if del_number_2 == 0:
        raise OwnError("Нельзя делить на ноль!!!")
except (ValueError, OwnError) as error:
    print(error)
else:
    print(f"Результат деления: {del_number_1 / del_number_2}")
