def int_func(word):
    a = word.split()
    b = []
    for i in a:
        if ord(i[0]) in range(65, 122, 1):
            b.append(i.title())
    return " ".join(b)


print(int_func(input("Введите слово/слова через пробел: ")))
