class Shape:
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def print_size(self):
        print("Shape is {} by {}".format(self.width, self.len))


class Square(Shape):
    def area(self):
        return self.width * self.len;

    def print_size(self):
        print("Square is {} by {}".format(self.width, self.len))


if __name__ == "__main__":
    a_square = Square(5, 10)
    a_square.print_size()
    print("a_square.area()={}".format(a_square.area()))

    a_shape = Shape(2, 5)
    a_shape.print_size()

    # b_square = Square(a_shape)
    # b_square.print_size()
    # print("b_square.area()={}".format(b_square.area()))
