def my_func(a, b):
    try:
        a = int(a)
        b = int(b)
        return round(a / b, 3)
    except ZeroDivisionError:
        return "На ноль не делится"
    except ValueError:
        return "Произошла ошибка. Может вы ввели буквы вместо цифр? Попробуйте снова."


print(my_func((input("Введите делимое: ")), input("Введите делитель: ")))
