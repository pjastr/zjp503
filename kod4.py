class Book:
    def __init__(self, title, year):
        self.title = title
        self.year = year

    def __lt__(self, other):
        return ((self.year, other.title) < (other.year, self.title))

    def __repr__(self):
        return f'{self.title} {self.year}'


b1 = Book('Potop', 1923)
b2 = Book('Potop', 1967)
b3 = Book("ogniem i mieczem", 1967)

lista = [b3, b2, b1]

print(lista)
lista.sort()
print(lista)