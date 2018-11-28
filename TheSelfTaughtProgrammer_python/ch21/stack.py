class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        # 参考 https://stackoverflow.com/questions/53513/how-do-i-check-if-a-list-is-empty
        return not self.items

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


def reverse(text):
    s = Stack()
    for c in text:
        s.push(c)
    reverse = ""
    while s.size():
        reverse += s.pop()
    print("text={}, reverse={}".format(text, reverse))


if __name__ == "__main__":
    stack = Stack()
    print(stack.is_empty())
    stack.push(1)
    print(stack.is_empty())
    print(stack.pop())
    print(stack.is_empty())

    stack = Stack()
    for i in range(0, 6):
        stack.push(i)
    print(stack.peek())
    print(stack.size())

    reverse("Hello")
