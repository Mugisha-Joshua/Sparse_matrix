from sparse_matrix import SparseMatrix
import os

def main():
    print("Choose the operation you want to perform:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    
    operation = input("Enter the number corresponding to the operation (1/2/3): ").strip()
    
    if operation not in ['1', '2', '3']:
        print("Invalid operation. Please choose 1, 2, or 3.")
        return
    
    matrix_file1 = input("Enter the name of the first matrix file (e.g., matrixfile1.txt): ").strip()
    matrix_file2 = input("Enter the name of the second matrix file (e.g., matrixfile2.txt): ").strip()
    result_file = input("Enter the name of the result file (e.g., result.txt): ").strip()
    
    try:
        matrix1 = SparseMatrix(matrix_file1)
        matrix2 = SparseMatrix(matrix_file2)
        
        if operation == '1':
            result = matrix1.add_with_padding(matrix2)
            operation_name = "addition"
        elif operation == '2':
            result = matrix1.subtract_with_padding(matrix2)
            operation_name = "subtraction"
        elif operation == '3':
            result = matrix1.multiply(matrix2)
            operation_name = "multiplication"
        
        with open(result_file, 'w') as file:
            file.write(f"Result of {operation_name}:\n")
            for row in result.matrix:
                for col in result.matrix[row]:
                    file.write(f"({row}, {col}, {result.get_element(row, col)})\n")
        
        print(f"Result has been saved to {result_file}")
    
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
