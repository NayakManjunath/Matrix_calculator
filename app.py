import numpy as np

# Function to get matrix input
def get_matrix():
    try:
        rows = int(input("Enter the number of rows: "))
        cols = int(input("Enter the number of columns: "))
        print("Enter the matrix elements row by row:")

        elements = []
        for _ in range(rows):
            row = list(map(float, input().split()))
            if len(row) != cols:
                raise ValueError("Number of columns doesn't match.")
            elements.append(row)

        return np.array(elements)

    except ValueError as e:
        print(f"Error: {e}")
        return None


# Matrix Operations
def matrix_operations(A, B):
    print("\nMatrix A:\n", A)
    print("\nMatrix B:\n", B)

    try:
        print("\nAddition:\n", A + B)
    except ValueError:
        print("Addition: Matrices must have the same dimensions.")

    try:
        print("\nSubtraction:\n", A - B)
    except ValueError:
        print("Subtraction: Matrices must have the same dimensions.")

    try:
        print("\nElement-wise Multiplication:\n", A * B)
    except ValueError:
        print("Element-wise Multiplication: Matrices must have the same dimensions.")

    try:
        print("\nDot Product:\n", np.dot(A, B))
    except ValueError:
        print("Dot Product: Number of columns in A must equal the number of rows in B.")

    print("\nTranspose of A:\n", A.T)
    print("\nTranspose of B:\n", B.T)

    try:
        print("\nDeterminant of A:\n", np.linalg.det(A))
    except np.linalg.LinAlgError:
        print("Determinant of A: Not applicable (Matrix must be square).")

    try:
        print("\nInverse of A:\n", np.linalg.inv(A))
    except np.linalg.LinAlgError:
        print("Inverse of A: Not invertible (Matrix must be square and non-singular).")


# Main Program
def main():
    print("Matrix Calculator")
    print("=================")
    print("\nInput Matrix A:")
    A = get_matrix()
    if A is None:
        return

    print("\nInput Matrix B:")
    B = get_matrix()
    if B is None:
        return

    matrix_operations(A, B)


if __name__ == "__main__":
    main()
