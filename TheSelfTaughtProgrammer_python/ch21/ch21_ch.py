from collections import deque
from stack import Stack

# 1
yesterday = deque("Yesterday")
reverse_yesterday = yesterday.copy()
reverse_yesterday.reverse()

# yesterday = "Yesterday"
# reverse_yesterday = ""
# for index in range(len(yesterday)):
#     reverse_yesterday += yesterday[-1 - index]

# yesterday = "Yesterday"
# r = Stack()
# for c in yesterday:
#     r.push(c)
# reverse_yesterday = ""
# while not r.is_empty():
#     reverse_yesterday += r.pop()

print("#1 '{}' -reverse-> '{}'".format("".join(yesterday), "".join(reverse_yesterday)))

# 2
stack = deque(range(1, 6))
r_stack = stack.copy()
r_stack.reverse()
print("#2 '{}' -reverse-> '{}'".format(", ".join(map(str, stack)), ", ".join(map(str, r_stack))))
