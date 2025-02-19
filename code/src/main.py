from sparse_matrix import SparseMatrix

def main():
    import sys
    
    if len(sys.argv) != 4:
        print("Usage: python main.py <operation> <matrix_file1> <matrix_file2>")
        sys.exit(1)
    
    operation = sys.argv[1]
    matrix_file1 = sys.argv[2]
    matrix_file2 = sys.argv[3]
    
    matrix1 = SparseMatrix(matrix_file1)
    matrix2 = SparseMatrix(matrix_file2)
    
    if operation == 'add':
        result = matrix1.add(matrix2)
    elif operation == 'subtract':
        result = matrix1.subtract(matrix2)
    elif operation == 'multiply':
        result = matrix1.multiply(matrix2)
    else:
        print("Invalid operation. Choose from 'add', 'subtract', or 'multiply'.")
        sys.exit(1)
    
    print("Resultant matrix:")
    for row in result.matrix:
        for col in result.matrix[row]:
            print(f"({row}, {col}, {result.get_element(row, col)})")

if __name__ == "__main__":
    main()
