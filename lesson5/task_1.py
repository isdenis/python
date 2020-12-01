with open("file_1.txt", "w", encoding="utf-8") as first_obj:
    q = []
    n = " "
    while n != "":
        n = input("Введите данные, после ввода нажмите enter. Для выхода просто нажмите enter: ")
        q.append(n)
    first_obj.write("\n".join(q))
