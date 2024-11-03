class DataProcessor:
    def __init__(self):
        self.numbers = []

    def add_number(self, number):
        self.numbers.append(number)

    def find_index(self, x):
        try:
            index = self.numbers.index(x) + 1
            return index
        except ValueError:
            return -1
