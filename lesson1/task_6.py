a = int(input("Напишите, сколько километров пробегает спортсмен за день: "))
print("Каждый день спортсмен увеличивает результат на 10 % относительно предыдущего")
b = int(input("Напишите, сколько километров всего пробежал спортсмен: "))
print("Сейчас посчитаем, сколко дней заняло у спортсмена пройти данный путь")
day = 1
while b > a:
    a = a * 1.1
    day += 1
    print(f"{day}-й день: {round(a,2)} км")
print(f"На {day} день спортсмен достиг результата - не менее {b} км")
