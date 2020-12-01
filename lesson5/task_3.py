with open("text_3.txt", "r", encoding="utf-8") as emp_salary:
    salary = 20000.0
    result = [line.split() for line in emp_salary]
    my_dict = {a: float(b) for a, b in result}
    print(f"Меньше {salary} руб. получают: {[i for i, b in my_dict.items() if b <= salary]}")
    print(f"Средняя величина дохода сотрудников составляет: {sum(my_dict.values()) / len(my_dict.values())}")
