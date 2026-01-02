import random

def generate_matrix(rows, cols):
    return [[random.randint(0, 10) for _ in range(cols)] for _ in range(rows)]

def multiply_matrices(A, B):
    r1, c1 = len(A), len(A[0])
    r2, c2 = len(B), len(B[0])

    if c1 != r2:
        raise ValueError("Matrix multiplication not possible (A.cols != B.rows).")

    result = [[0]*c2 for _ in range(r1)]

    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                result[i][j] += A[i][k] * B[k][j]

    return result

def print_matrix(M, title):
    print(f"\n{title}:")
    for row in M:
        print(" ".join(f"{x:3d}" for x in row))


# -------- MAIN --------
print("Matrix Multiplication (Random Values)")

r1 = int(input("Rows in Matrix A: "))
c1 = int(input("Columns in Matrix A: "))
r2 = int(input("Rows in Matrix B: "))
c2 = int(input("Columns in Matrix B: "))

# Generate random matrices based on user-given dimensions
A = generate_matrix(r1, c1)
B = generate_matrix(r2, c2)

print_matrix(A, "Matrix A (Auto-generated)")
print_matrix(B, "Matrix B (Auto-generated)")

result = multiply_matrices(A, B)
print_matrix(result, "A × B")
