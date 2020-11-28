from itertools import count, islice, cycle


def number_sum(a, b):
    try:
        a, b = int(a), int(b)
        if a < b:
            num_list = [i for i in islice(count(a), b - a + 1)]
            return num_list
        elif a > b:
            print("Начало цикла должно быть больше его окончания")
            return "Error"
    except ValueError:
        print("Допущена ошибка при вводе данных, попробуйте еще раз.")
        return "Error"


def number_repeat(c, d):
    try:
        repeat_list = [i for i in islice(cycle(d), int(c))]
        return repeat_list
    except ValueError:
        return "Допущена ошибка при вводе данных, попробуйте еще раз."
    except TypeError:
        return "Допущена ошибка при вводе данных, попробуйте еще раз."


n = (number_sum(input("Введите, с какого чила начинается цикл: "), input("Введите, каким числом заканчивается цикл: ")))
if n != "Error":
    r = (number_repeat(input("Введите сколько раз повторить полученный список: "), n))
    print(f"Итого у нас получился первый цикл: {n}, второй цикл: {r}")
elif n == "Error":
    print("Попробуйте заново!")
