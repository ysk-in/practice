import math


class Apple:
    def __init__(self, color, size, prefecture, price):
        self.color = color
        self.size = size
        self.prefecture = prefecture
        self.price = price

    def to_str(self):
        return "color={}, size={}, prefecture={}, price={}".format(self.color, self.size, self.prefecture, self.price)


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * math.pi


class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return (self.base * self.height) / 2


class Hexagon:
    def __init__(self, len1, len2, len3, len4, len5, len6):
        self.len1 = len1
        self.len2 = len2
        self.len3 = len3
        self.len4 = len4
        self.len5 = len5
        self.len6 = len6

    def calculate_perimeter(self):
        return self.len1 + self.len2 + self.len3 + self.len4 + self.len5 + self.len6


# 1
app1 = Apple("red", 10, "Shizuoka", 100)
print(app1.to_str())

# 2
print("Circle area={}".format(Circle(3).area()))

# 3
print("Circle area={}".format(Triangle(base=3, height=6).area()))

# 4
print("Hexagon calculate_perimeter={}".format(Hexagon(3, 3, 3, 3, 3, 3).calculate_perimeter()))
