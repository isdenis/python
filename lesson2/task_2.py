exchange = input("Введите любые элементы через пробел: ")
exchange_split = exchange.split()
exchange_split_reverse = []

b = len(exchange_split)
a = 0
while a < b:
    if (a + 1) < b:
        exchange_split_reverse.append(exchange_split[a + 1])
        exchange_split_reverse.append(exchange_split[a])
    else:
        exchange_split_reverse.append(exchange_split[a])
    a = a + 2

print(exchange_split_reverse)
