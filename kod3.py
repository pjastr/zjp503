class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"{self.name} {self.age}"

    def __lt__(self, other):
        # sortowanie wg wieku rosnąco
        # return self.age < other.age
        # sortowanie wg wieku malejąco
        return other.age < self.age


people = [Person("Jan", 20), Person("Tomasz", 33), Person("Anna", 15),
          Person("Anna", 27), Person("Sylwia", 44)]
print(people)
people.sort()
print(people)