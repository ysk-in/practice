# 1
def get_double(val):
    return int(val) ** 2


# 2
def print_str(str_to_print):
    print(str_to_print)


# 3
def req2_opt3(req1, req2, opt1="o1", opt2="o2", opt3="o3"):
    return ("req1=" + str(req1)
            + ", req2=" + str(req2)
            + ", opt1=" + str(opt1)
            + ", opt2=" + str(opt2)
            + ", opt3=" + str(opt3)
            )


# 4
def dev2(val):
    return int(val) % 2


def times4(val):
    return int(val) * 4


def to_float(val):
    try:
        return float(val)
    except BaseException as e:
        print("BaseException occurred. e=" + str(e))
        return None


# print(get_double(input("input value to double: ")))
# print_str("test print_str")
# print(req2_opt3("s_r1", "s_r2"))
# print(req2_opt3("s_r1", "s_r2", "s_o1", "s_o2"))
# print(times4(dev2(input("input dev2 -> times4: "))))
print(to_float(input("input to_float: ")))
