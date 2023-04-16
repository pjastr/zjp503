class Person(object):

    def __init__(self, firstname, lastname):
        self.first = firstname
        self.last = lastname

    def __lt__(self, other):
        if isinstance(other, Person):
            return (self.last, self.first) < (other.last, other.first)
        elif isinstance(other, int):
            return len(self.last) < other

    def __gt__(self, other):
        if isinstance(other, Person):
            return (self.last, self.first) > (other.last, other.first)
        elif isinstance(other, int):
            return len(self.last) > other

    def __repr__(self):
        return f"{self.first} {self.last}"


p1 = Person("Anna", "Nowak")
p2 = Person("Anna", "Kowalska")
print(p1 < 6)
print(p2 < p1)
print(6 < p1)