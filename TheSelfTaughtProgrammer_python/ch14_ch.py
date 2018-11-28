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
    square_list = []

    def __init__(self, length):
        super().__init__("Square")
        self.length = length
        self.square_list.append(self)
        self.index = len(self.square_list)

    def calculate_perimeter(self):
        return "Square length={}".format(self.length * 4)

    def add_length(self, length):
        self.length += length

    def __repr__(self):
        return "length=" + str(self.length)


def is_same(obj1, obj2):
    return obj1 is obj2


if __name__ == "__main__":
    print("#1")
    print("#2")
    square1 = Square(1)
    square2 = Square(2)
    square3 = Square(3)
    for s in Square.square_list:
        print("SquareIndex={}, calculate_perimeter={}".format(s.index, s.calculate_perimeter()))
        print(s)

    print("#3")
    print("is_same={}".format(is_same(Square(1), Square(1))))
    print("is_same={}".format(is_same("AAA", "AAA")))
