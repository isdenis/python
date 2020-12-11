class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def date_int(cls, date):
        day, month, year = map(int, date.split("-"))
        return cls(day, month, year)

    @staticmethod
    def date_valid(date):
        if date.day not in range(1, 32, 1):
            print("Был указан не верный день, попробуй еще.")
        else:
            print("Введенный день соответствует.")

        if date.month not in range(1, 13, 1):
            print("Был указан не верный месяц, попробуй еще.")
        else:
            print("Введенный месяц соответствует.")

        if date.year not in range(1, 9999, 1):
            print("Был указан не верный год, попробуй еще.")
        else:
            print("Введенный год соответствует.")


input_date = "25-12-2020"
my_date = Date.date_int(input_date)
Date.date_valid(my_date)
