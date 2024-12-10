'''Practical No 4 
Write a Python program to compute following computation on matrix: 
a) Addition of two matrices   B) Subtraction of two matrices 
c) Multiplication of two matrices d) Transpose of a matrix'''


print("Matrix A")
row1 = int(input("Enter number of rows for Matrix A: "))
col1 = int(input("Enter number of columns for Matrix A: "))
A = [[0 for j in range(col1)] for i in range(row1)]
for i in range(row1):
    for j in range(col1):
        A[i][j] = int(input(f"Enter element A[{i+1}][{j+1}]: "))
print("Matrix A:", A)


print("Matrix B")
row2 = int(input("Enter number of rows for Matrix B: "))
col2 = int(input("Enter number of columns for Matrix B: "))
B = [[0 for j in range(col2)] for i in range(row2)]
for i in range(row2):
    for j in range(col2):
        B[i][j] = int(input(f"Enter element B[{i+1}][{j+1}]: "))
print("Matrix B:", B)


def add():
    if row1 == row2 and col1 == col2:
        C = [[0 for j in range(col2)] for i in range(row2)]
        for i in range(row2):
            for j in range(col2):
                C[i][j] = A[i][j] + B[i][j]
        print("Result of Addition:")
        for row in C:
            print(row)
    else:
        print("Addition not possible. Matrices must have the same dimensions.")


def sub():
    if row1 == row2 and col1 == col2:
        C = [[0 for j in range(col2)] for i in range(row2)]
        for i in range(row2):
            for j in range(col2):
                C[i][j] = A[i][j] - B[i][j]
        print("Result of Subtraction:")
        for row in C:
            print(row)
    else:
        print("Subtraction not possible. Matrices must have the same dimensions.")


def Transpose():
    print("Transpose of Matrix A:")
    T_A = [[0 for j in range(row1)] for i in range(col1)]
    for i in range(row1):
        for j in range(col1):
            T_A[j][i] = A[i][j]
    for row in T_A:
        print(row)

    print("Transpose of Matrix B:")
    T_B = [[0 for j in range(row2)] for i in range(col2)]
    for i in range(row2):
        for j in range(col2):
            T_B[j][i] = B[i][j]
    for row in T_B:
        print(row)


def mul():
    if col1 == row2:
        C = [[0 for j in range(col2)] for i in range(row1)]
        for i in range(row1):
            for j in range(col2):
                C[i][j] = 0
                for k in range(col1):
                    C[i][j] += A[i][k] * B[k][j]
        print("Result of Multiplication:")
        for row in C:
            print(row)
    else:
        print("Multiplication not possible. Number of columns of A must be equal to number of rows of B.")

while True:
    print("\nEnter which operation you want to perform:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Transpose")
    print("5. Exit")
    choice = int(input("Choice: "))

    if choice == 1:
        add()
    elif choice == 2:
        sub()
    elif choice == 3:
        mul()
    elif choice == 4:
        Transpose()
    elif choice == 5:
        print("Exiting the program.")
        break
    else:
        print("Invalid choice! Please try again.")

