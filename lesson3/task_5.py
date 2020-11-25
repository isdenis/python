def my_func():
    result = 0
    while True:
        list1 = list(input("Введите любое количество чисел, разделенных пробелом "
                           "(или введите q для выхода): ").split())
        for i in list1:
            try:
                i = int(i)
                result += i
            except ValueError:
                if i == "q":
                    return f"Учитывая последние введенные числа сумма равна {result}. " \
                           f"Далее вы пожелали выйти, работа завершена."
        print(result)


print(my_func())
