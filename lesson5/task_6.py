with open("text_6.txt", "r", encoding="utf-8") as first_obj:
    my_list = [line.rstrip().split(":") for line in first_obj]
    my_dict = dict(my_list)
    for a, b in my_dict.items():
        d = []
        for i in b.split():
            d.append(''.join(c for c in i if c.isnumeric()))
        my_dict[a] = d

    for g, h in my_dict.items():
        d2 = []
        for i in h:
            if i != "":
                d2.append(int(i))
        my_dict[g] = sum(d2)
    print(my_dict)
