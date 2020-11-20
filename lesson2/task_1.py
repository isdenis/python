my_list = [1, 7.77, "text", False, [1, 2, 3], {4: "four", 5: "five"}, (6, 7)]
list_type = []

for a in range(len(my_list)):
    list_type.append(type(my_list[a]))
for b in enumerate(list_type):
    print(b)
