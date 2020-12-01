with open("file_2.txt", "r", encoding="utf-8") as first_obj:
    n = []
    for line in first_obj:
        n.append(line)
    print(n)
    print(f"Всего строк в файле: {len(n)}")
    num_str = 1
    for i in n:
        print(f"В строке {num_str} содержится {len((''.join(i).split()))} слова")
        num_str += 1
