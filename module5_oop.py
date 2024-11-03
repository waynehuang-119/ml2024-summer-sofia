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


def main():
    processor = DataProcessor()

    while True:
        try:
            n = int(input("Enter a positive integer N: "))
            if n > 0:
                break
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

    
    for i in range(n):
        while True:
            try:
                number = int(input(f"Enter number {i + 1}: "))
                processor.add_number(number)
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")

    
    while True:
        try:
            x = int(input("Enter an integer X to find in the previous inputs: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    
    result = processor.find_index(x)
    if result == -1:
        print("-1")
    else:
        print(result)

if __name__ == "__main__":
    main()