"""

"""


class QueueByTwoStack(object):

    def __init__(self):
        self.enqueue_stack = []
        self.dequeue_stack = []

    def enqueue(self, item):
        self.enqueue_stack.append(item)

    def dequeue(self):
        if self.dequeue_stack:
            return self.dequeue_stack.pop()

        if self.enqueue_stack:
            while self.enqueue_stack:
                self.dequeue_stack.append(self.enqueue_stack.pop())

            return self.dequeue_stack.pop()

        return None


if __name__ == "__main__":
    test_queue = QueueByTwoStack()
    test_queue.enqueue(1)
    test_queue.enqueue(2)
    test_queue.enqueue(3)

    print(test_queue.dequeue())
    print(test_queue.dequeue())
    print(test_queue.dequeue())
    print(test_queue.dequeue())
