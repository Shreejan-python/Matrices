def matrix(m, n):
    output = []
    for i in range(m):
        row = []
        for j in range(n):
            inp = int(input(f"Enter the matrix numbers[{i}][{j}]"))
            row.append(inp)
        output.append(row)
    return output

def minus(A, B):
    result = []
    for i in range(len(A)):#Number of rows
        row = []
        for j in range(len(A[0])):#Number of columns
            row.append(A[i][j] - B[i][j])
        result.append(row)
    return result


def main():
    m = int(input("Give the number of columns you want to have in your matrice : "))
    n = int(input("Give the number of digits you want to have in one matirce : "))

    print("Enter matrix A : ")
    A = matrix(m , n)
    print(f"The matrix A is {A}")

    print("Enter matrix B : ")
    B = matrix(m, n)
    print(f"The B matrix is {B}")

    m = minus(A, B)
    print(f"The difference between {A} and {B} is \n", m)

main()