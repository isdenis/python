from functools import reduce
import random

with open("file_5.txt", "w", encoding="utf-8") as digital_obj:
    first_list = [random.randint(1, 50) for i in range(10)]
    print(" ".join(map(str, first_list)), file=digital_obj)
with open("file_5.txt", "r", encoding="utf-8") as digital_obj:
    digit_sum = [line.split() for line in digital_obj]
    result = reduce(lambda a, x: a + x, [int(i) for i in digit_sum[0]])
    print(result)
