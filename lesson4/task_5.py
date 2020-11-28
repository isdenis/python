from functools import reduce

result_list = [reduce(lambda x, y: x + y, range(100, 1001, 2))]
print(result_list)
