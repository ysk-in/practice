import copy

tvs = ["GOT", "Nacros", "Vice"]


def print_dict():
    my_dict = {
        "k1": "v1",
        "k2": "v2",
        "k3": "v3"
    }
    for key in my_dict:
        print("key={}, val={}".format(key, my_dict[key]))


def print_tv():
    global tvs
    tv = copy.deepcopy(tvs)
    i = 0
    # for show in tv:
    #     new = tv[i]
    #     new = new.upper()
    #     tv[i] = new
    #     i += 1
    # これは無理っぽい
    # for show in tv:
    #     show = show.upper()
    # これは行ける
    for i in range(len(tv)):
        tv[i] = tv[i].upper()
    print(tv)


def test_enumerate():
    global tvs
    tv = copy.deepcopy(tvs)
    for i, t in enumerate(tv):
        print("i={}, t={}".format(i, t))
    pass


# print_dict()
# print_tv()

# name = "Ted"
# for n in name:
#     print(n)

test_enumerate()
print(tvs)
