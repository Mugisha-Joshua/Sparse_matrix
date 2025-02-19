
# Sparse Matrix Operations

This project provides a Python implementation for performing basic operations on sparse matrices, including addition, subtraction, and multiplication. Sparse matrices are stored efficiently to optimize both memory usage and runtime.

## Features
- Load sparse matrices from input files
- Perform matrix addition, subtraction, and multiplication
- Handle input variations and exceptions
- Save the results to an output file

## File Structure
```
/dsa/sparse_matrix/
    ├── main.py           # Main program to run the operations
    ├── sparse_matrix.py  # Implementation of the SparseMatrix class
    ├── utils.py          # Any helper functions or additional classes (if needed)
    ├── matrixfile1.txt   # Sample matrix files
    ├── matrixfile2.txt
    ├── matrixfile3.txt
    └── ...               # Additional sample matrix files

```

## Prerequisites
- Python 3.x

## Installation
1. Clone the repository to your local machine:
    ```sh
    git https://github.com/Mugisha-Joshua/Sparse_matrix.git
    ```

2. Navigate to the project directory:
    ```sh
    cd sparse_matrix
    ```

## Usage
1. Ensure you have your sparse matrix input files in the project directory. Example input file format:
    ```
    rows=8433
    cols=3180
    (0, 381, -694)
    (0, 128, -838)
    (0, 639, 857)
    (0, 165, -933)
    (0, 1350, -89)
    ```

2. Run the main program:
    ```sh
    python main.py
    ```

3. Follow the prompts:
    - Choose the operation you want to perform (1 for Addition, 2 for Subtraction, 3 for Multiplication).
    - Enter the names of the input matrix files (e.g., matrixfile1.txt, matrixfile2.txt).
    - Enter the name of the result file (e.g., result.txt).

4. The result will be saved to the specified result file.

## Example
```sh
$ python main.py
Choose the operation you want to perform:
1. Addition      
2. Subtraction   
3. Multiplication
Enter the number corresponding to the operation (1/2/3): 1
Enter the name of the first matrix file (e.g., matrixfile1.txt): matrixfile1.txt
Enter the name of the second matrix file (e.g., matrixfile2.txt): matrixfile2.txt
Enter the name of the result file (e.g., result.txt): addition_result.txt
Result has been saved to addition_result.txt
```

## Error Handling
- If the dimensions of the matrices do not match for addition or subtraction, the program will pad the smaller matrix with zeros to match the dimensions of the larger matrix.
- The program will handle variations in the input file format and throw appropriate errors for invalid formats.

## Collaborators
- **JOSHUA OCHEL MUGISHA**
- **COPILOT AI**
- **CLAUDE AI**

## Contact
If you have any questions or suggestions, feel free to open an issue or contact the project maintainers at o.mugisha2@alustudent.com.
```
