import collections


def count_char(string):
    count_dict = {}
    for c in string:
        if c in count_dict:
            count_dict[c] += 1
        else:
            count_dict[c] = 1
    print(count_dict)


def count_char_default_dict(string):
    count_dict = collections.defaultdict(int)
    for c in string:
        count_dict[c] += 1
    print(count_dict)


s = "Dynastyあああ"
count_char(s)
count_char_default_dict(s)
print(collections.Counter(s))
