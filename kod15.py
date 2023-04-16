class Calculator:

    def __init__(self, x, y):
        if not isinstance(x, (int, float)):
            raise TypeError("Wrong type of x")
        if not isinstance(y, (int, float)):
            raise TypeError("Wrong type of y")
        self.x = x
        self.y = y

    def dodaj(self):
        return self.x + self.y

    def podziel(self):
        try:
            return self.x / self.y
        except ZeroDivisionError:
            print("Division by zero!")


c = Calculator(2, 6)
print(c.dodaj())
print(c.podziel())
c2 = Calculator(2, 0)
print(c2.dodaj())
print(c2.podziel())