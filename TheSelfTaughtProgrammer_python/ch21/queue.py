class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def enqueue(self, item):
        return self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


def exec_assert(actual, expected, fail_msg=''):
    assert actual == expected, "{}expected={}, actual={}.".format(fail_msg, expected, actual)


def test_en_de_queue():
    q = Queue()

    exec_assert(q.size(), 0)

    for i in range(5):
        q.enqueue(i)
    exec_assert(q.size(), 5)
    exec_assert(q.items, [4, 3, 2, 1, 0])

    q.dequeue()
    q.dequeue()
    exec_assert(q.size(), 3)
    exec_assert(q.items, [4, 3, 2])


def test_is_empty():
    q = Queue()
    expected = True
    assert q.is_empty(), "test_is_empty failed! expected={}, actual={}.".format(expected, not expected)

    q.enqueue(1)
    expected = False
    assert not q.is_empty(), "test_is_empty failed! expected={}, actual={}.".format(expected, not expected)


if __name__ == "__main__":
    print("__debug__ = " + str(__debug__))
    if __debug__:
        test_en_de_queue()
        test_is_empty()
