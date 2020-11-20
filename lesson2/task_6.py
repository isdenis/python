print("Добро пожаловать в аналитику закупок. Сейчас нужно будет вводить данные о товарах и иинформацию о них")
begin = input("Хотите продолжить? Да/Нет: ")
analytics = []
analytics_result = {}
product = ()
product_dict = {}
product_num = ()
i = 1
if begin.lower() == "нет":
    print("Еще увидимся!")
elif begin.lower() == "да":
    product_num = int(input("Введите количество товара, которые хотите добавить: "))
    while i <= product_num:
        print("*" * 50)
        print(f"Сейчас вы вносите данные по {i} товару.")
        print("*" * 50)
        name = input("Введите название: ")
        price = input("Введите сумму: ")
        count = input("Введите количество: ")
        unit = input("Введите единицу измерения (например, шт.): ")
        product_dict = dict({"Название ": name, "Цена ": price, "Количество": count, "Ед.": unit})
        product = (i, product_dict)
        analytics.append(product)
        print("_" * 120)
        print(f"Вы ввели Ваш {i} товар, у которого следующие характеристики: \n"
              f"{product}")
        print("_" * 120)
        i += 1

for i in analytics:
    for key, value in i[1].items():
        if key in analytics_result:
            analytics_result.get(key).append(value)
        else:
            analytics_result.update({key: [value]})

print("*" * 120)
print(f"Аналитика по введенным {product_num} товарам: ")
for key, value in analytics_result.items():
    print(f" {key}: {str(value)[1:-1]}")
print("*" * 120)
