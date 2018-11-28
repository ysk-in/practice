class Orange:
    def __init__(self, weight=0, color=0):
        self.weight = weight
        self.color = color
        self.mold = 0
        print("Created!")

    def rot(self, days, temp):
        """tmp(温度)は摂氏"""
        self.mold = days * temp


if __name__ == "__main__":
    or1 = Orange(color="dark orange", weight=10)
    print("orl.weight={}, orl.color={}".format(or1.weight, or1.color))

    or2 = Orange()
    print("orl2.weight={}, orl2.color={}".format(or2.weight, or2.color))

    print("or1.weight={}, or1.color={}, or1.mold={}".format(or1.weight, or1.color, str(or1.mold)))
    or1.rot(3, 10)
    print("or1.weight={}, or1.color={}, or1.mold={}".format(or1.weight, or1.color, str(or1.mold)))
