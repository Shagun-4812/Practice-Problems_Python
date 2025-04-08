def generate_magic_square(n):
    if n < 3:
        print("Magic squares are not possible for n < 3.")
        return None

    magic_square = [[0] * n for _ in range(n)]

    i, j = 0, n // 2  

    for num in range(1, n * n + 1):
        magic_square[i][j] = num 

        
        new_i, new_j = (i - 1) % n, (j + 1) % n

        if magic_square[new_i][new_j] != 0:
            i = (i + 1) % n
        else:
            i, j = new_i, new_j

    return magic_square


def print_matrix(matrix):
    for row in matrix:
        print(" ".join(f"{num:3}" for num in row))


def main():
    n = int(input("Enter the order of the square matrix (n >= 3): "))
    magic_square = generate_magic_square(n)

    if magic_square:
        print("\nGenerated Magic Square:")
        print_matrix(magic_square)

        
        magic_constant = sum(magic_square[0])
        print(f"\nMagic Constant (Sum of each row, column, and diagonal): {magic_constant}")


if __name__ == "__main__":
    main()