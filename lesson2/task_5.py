my_list = [8, 8, 7, 5, 3, 3, 2]
print(f"У нас есть рейтинг: {my_list}. Вам необходимо добавить значения в данный рейтинг.")
user_element = int(input("Введите новый элемент рейтинга, в виде цифры: "))
a = 0
index = 0
index_second = 0

for a in my_list:
    if user_element <= a:
        index += 1
my_list.insert(index, user_element)

print(f"Обновленный рейтинг, с учетом веденного вами значения: {my_list}")
