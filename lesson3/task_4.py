def my_func(x, y):
    try:
        x = float(x)
        y = int(y)
        i = 1
        result = x
        while i < (y * -1):
            result = result * x
            i += 1
        result = 1 / result
        return result
    except ValueError:
        return "Произошла ошибка. Может вы ввели буквы вместо цифр? Попробуйте снова."


print(my_func(input("Введите действительное положительное число x: "),
              input("Введите целое отрицательное число y: ")))
