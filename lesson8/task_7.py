class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @classmethod
    def complex1(cls, num):
        a, b = map(int, num.split())
        return cls(a, b)

    def __add__(self, other):
        return ComplexNumber(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return ComplexNumber(self.a * other.a - self.b * other.b, self.a * other.b + other.a * self.b)

    def __str__(self):
        if self.b > 0:
            return f"{self.a}+{self.b}i"
        else:
            return f"{self.a}{self.b}i"


my_num1 = ComplexNumber.complex1(input("Введите через пробел два числа первого комплексного числа: "))
my_num2 = ComplexNumber.complex1(input("Введите через пробел два числа второго комплексного числа: "))

print(my_num1 + my_num2)
print(my_num1 * my_num2)
