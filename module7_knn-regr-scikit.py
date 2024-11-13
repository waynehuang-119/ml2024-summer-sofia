import numpy as np
from sklearn.neighbors import KNeighborsRegressor

class DataProcessor:
    def __init__(self):
        self.points = []

    def add_point(self, x, y):
        self.points.append((x, y))

    def calculate_distance(self, x1, x2):
        # Euclidean distance
        return np.sqrt((x1 - x2) ** 2)

    def calculate_variance(self):
        y_values = [y for _, y in self.points]
        return np.var(y_values)
    
    def k_nearest_neighbors(self, x_query, k):
        X = np.array([x for x, y in self.points]).reshape(-1, 1)
        y = np.array([y for x, y in self.points]) 

        knn = KNeighborsRegressor(n_neighbors=k)
        knn.fit(X, y)

        return knn.predict(np.array([[x_query]]))[0]


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

    while True:
        try:
            k = int(input(f"Enter a positive integer k (<= {n}): "))
            if 1 <= k <= n:
                break
            else:
                print(f"k should be between 1 and {n}.")
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
            x_query = float(input("Enter X to query: "))
            break
        except ValueError:
            print("Invalid input. Please enter a real number.")

    try:
        result = processor.k_nearest_neighbors(x_query, k)
        print(f"The result of {k}-NN Regression for X = {x_query} is Y = {result}")

        variance = processor.calculate_variance()
        print(f"The variance of the labels in the training dataset is: {variance}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
