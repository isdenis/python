from functools import reduce


def generator(n):
    try:
        yield reduce(lambda x, y: x * y, range(1, int(n) + 1))
    except TypeError:
        yield "Ошибка, попробуй еще."
    except ValueError:
        yield "Ошибка, попробуй еще."


for i in generator(input("Введите число, факториал которого нужно посчитать: ")):
    print(f"Факториал равен: {i}")
