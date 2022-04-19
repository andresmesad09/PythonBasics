import numpy as np


def main():
    # ----
    # 1) Use np.arange and np.reshape to create a 3x3 that includes numbers 3 - 11
    # ----
    A = np.arange(3, 12).reshape(3, 3)
    print(f"Matrix is: \n{A}\nShape: {A.shape}\nDiagonal: {A.diagonal()}\nFlatten Values: {A.flatten()}")

    # ----
    # 2) Display the min, max and median of all entries in A
    # ----
    print(f"Min: {A.min()}")
    print(f"Max: {A.max()}")
    print(f"Mean: {A.mean()}")

    # ----
    # 3) Square every entri using **
    # ----
    B = A ** 2
    print(f"B is: \n{B}")

    # ----
    # 4) Use np.vstack to stack A on top of B -> C
    # ----
    C = np.vstack([A, B])
    print(f"C is: \n{C}")

    # ----
    # 5) Use @ to get the matrix product
    # ----
    matrix_prod = A @ B
    print(f"matrix_prod is: \n{matrix_prod}")

    # ----
    # 6) Reshape C into an array of dimensions 3 x 3 x 2
    # ----
    new_c = C.reshape(3,3,2)
    print(f"new_c is: \n{new_c}")


if __name__ == '__main__':
    main()