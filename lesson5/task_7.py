import json

with open("text_7.txt", "r", encoding="utf-8") as firm_obj:
    my_dict = {}
    profit = 0
    len_profit = 0
    for line in firm_obj:
        n = line.split()
        my_dict[n[0]] = int(n[2]) - int(n[3])
    for i in my_dict.values():
        if i >= 0:
            profit = profit + i
            len_profit += 1
    my_dict_aver = {"average_profit": profit / len_profit}
    result = [my_dict, my_dict_aver]
    print(result)

with open("my_json.json", "w", encoding="utf-8") as write_f:
    json.dump(result, write_f, sort_keys=False, indent=4, ensure_ascii=False, separators=(',', ': '))
