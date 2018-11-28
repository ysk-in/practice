line = "-" * 3
line1 = list()
for l in line:
    print(l)
    line1.append(l)
print(line1)

print("".join(line1))

word_list = [
    "cat",
    "dog",
    "python",
    "perl",
    "clang",
    "golang",
    "java",
    "scala",
    "kotlin",
    "ruby"
]
print(len(word_list))
for i, word in enumerate(word_list):
    print("i={}, word={}".format(i, word))
