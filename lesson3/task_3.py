def my_func(a, b, c):
    result = [int(a), int(b), int(c)]
    result.sort()
    return f"Два наибольших значения, которые вы ввели, являются: {result[-2:]}."


print(my_func(input("Введите первое число: "), input("Введите второе число: "), input("Введите третье число: ")))
