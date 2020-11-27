from sys import argv


def salary_func():
    try:
        script_name, output_hours, rate_hour, bonus = argv
        print(f"Выработка в часах составила: {output_hours}\n"
              f"Ставка в час: {rate_hour}\n"
              f"Премия: {bonus}\n"
              f"Заработная плата сотрудника: {int(output_hours) * int(rate_hour) + int(bonus)}")
    except ValueError:
        print("Допущена ошибка при вводе данных, попробуйте еще раз.")


salary_func()
