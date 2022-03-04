from msilib.schema import Class


def print_hello():
    print('Hello')

class MyClass:
    def __init__(self, word) -> None:
        self.word = word

    def pring(self):
        print(self.word)
