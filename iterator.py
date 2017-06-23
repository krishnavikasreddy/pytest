"This is to test the iterator in python"

class IterateNumber(object):
    """
    Example of a Iterator example
    """
    def __init__(self, limit):
        self.number = 0
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        print('vikas')

    def next(self):
        "next iteration"
        yield self.number

def GenerateNumber(initial):
    while initial < 100:
        yield initial
        initial += 1

if __name__ == "__main__":
    V = IterateNumber(10)
    next(V)
