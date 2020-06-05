class Stack:
    """
    A class to implements the properties of Stack.

    You can push, pop from the stack and get the length of storage.
    """

    def __init__(self):
        self.storage = []

    def __repr__(self):
        return f"stack: {self.storage}"

    def push(self, value):
        return self.storage.append(value)

    def pop(self):
        if self.size() > 0:
            self.storage.pop()
        else:
            return None

    def size(self):
        return len(self.storage)
