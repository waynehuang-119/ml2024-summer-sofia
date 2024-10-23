
if __name__ == "__main__":
    
    N = int(input("Enter a positive integer N: "))
    
    numbers = []

    for i in range(N):
        num = int(input(f"Enter number {i + 1}: "))
        numbers.append(num)

    X = int(input("Enter an integer X to find in the previous inputs: "))

    if X in numbers:
        print(numbers.index(X) + 1)
    else:
        print("-1")
