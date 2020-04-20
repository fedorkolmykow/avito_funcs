class NotIterable:
    def __init__(self, value):
        self.value = value


class SimpleIterator:
    def __init__(self, limit):
        self.limit = limit
        self.counter = 0

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return 1
        else:
            raise StopIteration

    def __iter__(self):
        return self


class SomeIterable:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return iter(self.value)