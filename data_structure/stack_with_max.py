"""

"""


class StackWithMax(object):
    """

    """
    def __init__(self):
        self.content = []
        self.max_heap = []

    def push(self, val):
        """

        :param val:
        :return:
        """
        self.content.append(val)

        if self.max_heap:
            self.max_heap.append(max(val, self.max_heap[-1]))
        else:
            self.max_heap.append(val)

    def pop(self):
        """

        :return:
        """
        try:
            current = self.content.pop()
        except IndexError:
            return None
        else:
            self.max_heap.pop()
            return current

    def max(self):
        """

        :return:
        """
        try:
            return self.max_heap[-1]
        except IndexError:
            return None


if __name__ == "__main__":
    test_stack = StackWithMax()
    print(test_stack.max())

    test_stack.push(10)
    test_stack.push(1)
    test_stack.push(100)

    print(test_stack.max())

    current_item = test_stack.pop()
    print(current_item)

    print(test_stack.max())
