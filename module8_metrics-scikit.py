import numpy as np
from sklearn.metrics import precision_score, recall_score

class DataProcessor:
    def __init__(self):
        self.points = []

    def add_point(self, x, y):
        self.points.append((x, y))

    def calculate_precision_and_recall(self):
        y_true = np.array([x for x, y in self.points])  
        y_pred = np.array([y for x, y in self.points])  


        precision = precision_score(y_true, y_pred)
        recall = recall_score(y_true, y_pred)

        return precision, recall


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
                x = int(input(f"Enter x value (ground truth) for point {i + 1} (0 or 1): "))
                y = int(input(f"Enter y value (predicted class) for point {i + 1} (0 or 1): "))
                if x in [0, 1] and y in [0, 1]:
                    processor.add_point(x, y)
                    break
                else:
                    print("Please enter values as either 0 or 1.")
            except ValueError:
                print("Invalid input. Please enter valid integers (0 or 1).")
   
    # Calculate Precision and Recall
    precision, recall = processor.calculate_precision_and_recall()
    print(f"Precision: {precision}")
    print(f"Recall: {recall}")


if __name__ == "__main__":
    main()
