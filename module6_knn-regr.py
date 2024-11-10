import numpy as np

class DataProcessor:
    def __init__(self):
        self.points = []

    def add_point(self, x, y):
        self.points.append((x, y))

    def calculate_distance(self, x1, x2):
        # Euclidean distance
        return np.sqrt((x1 - x2) ** 2)

    def k_nearest_neighbors(self, x_query, k):
        distances = []
        for x, y in self.points:
            distance = self.calculate_distance(x, x_query)
            distances.append((distance, y))
        
        distances.sort(key=lambda item: item[0])
        
        # Find the k-th distance value
        kth_distance = distances[k - 1][0]

        # Include all points with the same distance as the k-th nearest
        k_nearest = [point for point in distances if point[0] <= kth_distance]

        y_values = [y for _, y in k_nearest]
        return np.mean(y_values)


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
                x = float(input(f"Enter x value for point {i + 1}: "))
                y = float(input(f"Enter y value for point {i + 1}: "))
                processor.add_point(x, y)
                break
            except ValueError:
                print("Invalid input. Please enter valid real numbers.")

    while True:
        try:
            k = int(input(f"Enter a positive integer k (<= {n}): "))
            if 1 <= k <= n:
                break
            else:
                print(f"k should be between 1 and {n}.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

    while True:
        try:
            x_query = float(input("Enter X to query: "))
            break
        except ValueError:
            print("Invalid input. Please enter a real number.")

    try:
        result = processor.k_nearest_neighbors(x_query, k)
        print(f"The result of {k}-NN Regression for X = {x_query} is Y = {result}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
