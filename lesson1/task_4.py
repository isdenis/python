number = int(input("Введи целое положительное число: "))
max = 0
while number > 0:
    i = number % 10
    number = number // 10
    if i > max:
        max = i
print(max)
