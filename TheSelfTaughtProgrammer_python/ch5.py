print("aaa".upper())
print("aaa".replace("a", "b"))

fruit = ["Ap", "Or", "Pe"]
print(fruit)
fruit.append("Ba")
fruit.append(100)
fruit.append(1.2)
fruit.append(True)
fruit.append(None)
fruit.append("")
fruit.append("e")
print(fruit)

print("--- foreach start ---")
for f in fruit:
    print(f)
print("--- foreach end ---")

print("--- for start ---")
print("len=" + str(len(fruit)))
for i in range(len(fruit)):
    print(fruit[i])
print("--- for end ---")

print("--- for(try) start ---")
for i in range(20):
    try:
        print(fruit[i])
    except BaseException as e:
        print("ignore exception. e=" + str(e))
print("--- for(try) end ---")

print("--- for start ---")
for i in range(len(fruit)):
    if (i % 2) == 0:
        fruit[i] = ""
print("--- for end ---")
print(fruit)

print("--- pop Loop start")
while True:
    try:
        fruit.pop()
    except BaseException as e:
        print("pop failed. e=" + str(e))
        break
print("--- pop Loop end")

colors = ["Red", "Blue", "Yello"]
nums = ["1", "2", "3", "4"]
colors_nums = colors + nums
print(colors_nums)

# tuple
my_tuple = ("a", "b", "c")
try:
    my_tuple[0] = "1"
except BaseException as e:
    print("tuple append error. e=" + str(e))

# dict
dict1 = dict()
dict1[1] = "one"
dict1["2"] = "two"
print(dict1[int("1")])
print(dict1)
dict1 = {
    "Apple": "Red",
    "Banana": "Yellow",
    "Orange": "Orange"
}
print(dict1)

print("Apple" in dict1)

if "Apple" in dict1:
    print("dict1 has key \"Apple\"")

print("END")
