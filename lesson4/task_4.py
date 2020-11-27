import random

a = int(input("Введите начальную цифру для генерации: "))
b = int(input("Введите последнюю цифру для генерации: "))
c = int(input("Введите количество цифру в списке: "))

first_list = [random.randint(a, b) for i in range(c)]
result_list = [i for i in first_list if first_list.count(i) == 1]

print(f"Сгенерированный исходный список:\n {first_list}\n"
      f"Новый список, в котором элементы не имели повторений:\n {result_list}")