import random

a = int(input("Введите начальную цифру для генерации: "))
b = int(input("Введите последнюю цифру для генерации: "))
c = int(input("Введите количество цифру в списке: "))

first_list = [random.randint(a, b) for i in range(c)]
result_list = [first_list[n] for n in range(1, len(first_list)) if first_list[n] > first_list[n - 1]]

print(f"Сгенерированный исходный список:\n {first_list}\n"
      f"Новый список, значения в котором больше предыдущего элемента:\n {result_list}")
