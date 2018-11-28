# 4章

g1 = 1
g2 = 2
g3 = 3


def f(x):
    return x * 2


def test_func_none():
    z = 1 + 1


def is_age_under_21(age):
    int_age = int(age)
    if int_age < 21:
        print("You are young!")
    else:
        print("Wow, you are old!")


def is_age_under_21_3times():
    for i in range(3):
        is_age_under_21(input("Enter your age: "))


def fx(x=2):
    return x ** x


def add_it(x, y=10):
    return x + y


def print_global_var():
    global g1
    print(str(g1) + str(g2) + str(g3))
    # global g1 = 100
    g1 = 100
    print(str(g1) + str(g2) + str(g3))


def divide_a_b(a, b):
    print("a=" + str(a) + ", b=" + str(b))
    print(int(a) / int(b))


def add(x, y):
    """
  Returns x + y.
  :param x: int.
  :param y: int.
  :return: int sum of x and y.
  """
    return int(x) + int(y)


# is_age_under_21(input("Enter your age: "))
# is_age_under_21_3times()

print(fx(3))
print(fx())

print(add_it(2))
print(add_it(2, 3))

print_global_var()
print_global_var()

try:
    divide_a_b(input("a: "), input("b: "))
    # divide_a_b(4, 2)
except(ZeroDivisionError, ValueError):
    print("ZDE or VE")
except ZeroDivisionError:
    print("b cannot be zero.")
except ValueError:
    print("b must be a number.")

print(add(1, "2"))
