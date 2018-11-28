class Rectangle:
    recs = []

    def __init__(self, w, l):
        self.width = w
        self.len = l
        self.recs.append((self.width, self.len))

    def print_size(self):
        print("{} by {}".format(self.width, self.len))


class Lion:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


class AlwaysPositive:
    def __init__(self, number):
        self.n = number

    def __add__(self, other):
        return abs(self.n + other.n)


class Person:
    def __init__(self):
        self.name = "Bob"


if __name__ == "__main__":
    # r1 = Rectangle(10, 24)
    # r2 = Rectangle(20, 40)
    # r3 = Rectangle(100, 200)
    # print(Rectangle.recs)

    # lion1 = Lion("Dilbert")
    # print(lion1)

    # p3 = 3
    # n5 = -5
    # a3 = AlwaysPositive(p3)
    # a5 = AlwaysPositive(n5)
    # print("{} {}".format(a3 + a5, p3 + n5))

    bob = Person()
    same_bob = bob
    print(bob is same_bob)

    another_bob = Person()
    print(bob is another_bob)

    print("aaa" is "a"*3)
