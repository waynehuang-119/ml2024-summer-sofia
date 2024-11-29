import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score

class DataProcessor:
    def __init__(self):
        self.data_x = []
        self.data_y = []

    def add_point(self, x, y):
        """Adds a single (x, y) pair to the dataset."""
        self.data_x.append(x)
        self.data_y.append(y)

    def get_data(self):
        """Returns the dataset as NumPy arrays."""
        return np.array(self.data_x).reshape(-1, 1), np.array(self.data_y)

    def read_data_set(self, num_points, set_name):
        """Reads a dataset of (x, y) pairs from the user."""
        print(f"Enter {num_points} (x, y) pairs for the {set_name} set:")
        for i in range(num_points):
            while True:
                try:
                    x = float(input(f"Enter x value for pair {i + 1}: "))
                    y = int(input(f"Enter y value for pair {i + 1} (non-negative integer): "))
                    if y >= 0:
                        self.add_point(x, y)
                        break
                    else:
                        print("y value must be a non-negative integer.")
                except ValueError:
                    print("Invalid input. Please enter valid values.")

def main():
    # Read training set
    train_processor = DataProcessor()
    while True:
        try:
            n = int(input("Enter a positive integer N (number of training pairs): "))
            if n > 0:
                break
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")
    train_processor.read_data_set(n, "training")
    train_x, train_y = train_processor.get_data()

    # Read test set
    test_processor = DataProcessor()
    while True:
        try:
            m = int(input("Enter a positive integer M (number of test pairs): "))
            if m > 0:
                break
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")
    test_processor.read_data_set(m, "test")
    test_x, test_y = test_processor.get_data()

    # Dynamically set the range of k based on the number of training samples
    max_k = min(10, len(train_x) - 1)  # Avoid k equal to or greater than number of samples
    param_grid = {'n_neighbors': list(range(1, max_k + 1))}  # k values from 1 to max_k
    knn = KNeighborsClassifier()

    # Try using 5-fold cross-validation
    try:
        grid_search = GridSearchCV(estimator=knn, param_grid=param_grid, scoring='accuracy', cv=5)
        grid_search.fit(train_x, train_y)
    except ValueError:
        # Fall back to 2-fold cross-validation if there are issues with 5 folds
        print("Error: n_splits=5 cannot be greater than the number of samples in one class. Trying with 2 splits.")
        grid_search = GridSearchCV(estimator=knn, param_grid=param_grid, scoring='accuracy', cv=2)
        grid_search.fit(train_x, train_y)

    # Output the best k and its accuracy
    best_k = grid_search.best_params_['n_neighbors']
    best_accuracy = grid_search.best_score_
    print(f"\nBest k: {best_k}")
    print(f"Cross-validation Accuracy for best k: {best_accuracy:.4f}")

    # Evaluate on the test set
    best_knn = grid_search.best_estimator_
    test_predictions = best_knn.predict(test_x)
    test_accuracy = accuracy_score(test_y, test_predictions)
    print(f"Test Accuracy for best k: {test_accuracy:.4f}")

if __name__ == "__main__":
    main()
