class Shape:
    def __init__(self, shape_type="Shape"):
        self.shape_type = shape_type
        pass

    def what_am_i(self):
        return "I am a " + self.shape_type


class Rectangle(Shape):
    def __init__(self, width, length):
        super().__init__("Rectangle")
        self.width = width
        self.length = length

    def calculate_perimeter(self):
        return "Rectangle length={}".format(self.width * 2 + self.length * 2)


class Square(Shape):
    def __init__(self, length):
        super().__init__("Square")
        self.length = length

    def calculate_perimeter(self):
        return "Square length={}".format(self.length * 4)

    def add_length(self, length):
        self.length += length


class Horse:
    def __init__(self, rider):
        self.rider = rider


class Rider:
    def __init__(self, name):
        self.name = name


if __name__ == "__main__":
    print("#1")
    rec1 = Rectangle(3, 6)
    print("rec1.calculate_perimeter()={}".format(rec1.calculate_perimeter()))
    squ1 = Square(4)
    print("squ1.calculate_perimeter()={}".format(squ1.calculate_perimeter()))

    print("#2")
    squ1.add_length(3)
    print("after add_length(3) squ1.calculate_perimeter()={}".format(squ1.calculate_perimeter()))
    squ1.add_length(-6)
    print("after add_length(-6) squ1.calculate_perimeter()={}".format(squ1.calculate_perimeter()))

    print("#3")
    print("rec1.what_am_i()={}".format(rec1.what_am_i()))
    print("squ1.what_am_i()={}".format(squ1.what_am_i()))
    sha1 = Shape()
    print("sha1.what_am_i()={}".format(sha1.what_am_i()))

    print("#4")
    rider = Rider("Rider1san")
    horse = Horse(rider)
    print("horse.rider.name={}".format(horse.rider.name))
