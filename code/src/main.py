from sparse_matrix import SparseMatrix

def main():
    import sys
    
    print("Choose the operation you want to perform:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    
    operation = input("Enter the number corresponding to the operation (1/2/3): ").strip()
    
    if operation not in ['1', '2', '3']:
        print("Invalid operation. Please choose 1, 2, or 3.")
        sys.exit(1)
    
    matrix_file1 = input("Enter the path to the first matrix file: ").strip()
    matrix_file2 = input("Enter the path to the second matrix file: ").strip()
    
    try:
        matrix1 = SparseMatrix(matrix_file1)
        matrix2 = SparseMatrix(matrix_file2)
        
        if operation == '1':
            result = matrix1.add(matrix2)
            print("Result of addition:")
        elif operation == '2':
            result = matrix1.subtract(matrix2)
            print("Result of subtraction:")
        elif operation == '3':
            result = matrix1.multiply(matrix2)
            print("Result of multiplication:")
        
        for row in result.matrix:
            for col in result.matrix[row]:
                print(f"({row}, {col}, {result.get_element(row, col)})")
    
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
