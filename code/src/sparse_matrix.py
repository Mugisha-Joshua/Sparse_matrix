class SparseMatrix:
    def __init__(self, matrix_file_path=None, num_rows=None, num_cols=None):
        if matrix_file_path:
            self.num_rows, self.num_cols, self.matrix = self._read_matrix_from_file(matrix_file_path)
        else:
            self.num_rows = num_rows
            self.num_cols = num_cols
            self.matrix = {}

    def _read_matrix_from_file(self, matrix_file_path):
        try:
            with open(matrix_file_path, 'r') as file:
                lines = file.readlines()
            
            num_rows = int(lines[0].split('=')[1].strip())
            num_cols = int(lines[1].split('=')[1].strip())
            matrix = {}
            
            for line in lines[2:]:
                line = line.strip()
                if line and line.startswith('(') and line.endswith(')'):
                    elements = line[1:-1].split(',')
                    if len(elements) != 3:
                        raise ValueError("Input file has wrong format")
                    row, col, value = map(int, elements)
                    if row not in matrix:
                        matrix[row] = {}
                    matrix[row][col] = value
                elif line:
                    raise ValueError("Input file has wrong format")
            
            return num_rows, num_cols, matrix
        except Exception as e:
            raise ValueError(f"Error reading matrix from file: {str(e)}")

    def get_element(self, curr_row, curr_col):
        return self.matrix.get(curr_row, {}).get(curr_col, 0)

    def set_element(self, curr_row, curr_col, value):
        if curr_row not in self.matrix:
            self.matrix[curr_row] = {}
        self.matrix[curr_row][curr_col] = value

    def add(self, other):
        if self.num_rows != other.num_rows or self.num_cols != other.num_cols:
            raise ValueError("Matrices dimensions do not match for addition")
        
        result = SparseMatrix(num_rows=self.num_rows, num_cols=self.num_cols)
        
        for row in self.matrix:
            for col in self.matrix[row]:
                result.set_element(row, col, self.get_element(row, col) + other.get_element(row, col))
        
        for row in other.matrix:
            for col in other.matrix[row]:
                if (row not in self.matrix) or (col not in self.matrix[row]):
                    result.set_element(row, col, other.get_element(row, col))
        
        return result
    
    def subtract(self, other):
        if self.num_rows != other.num_rows or self.num_cols != other.num_cols:
            raise ValueError("Matrices dimensions do not match for subtraction")
        
        result = SparseMatrix(num_rows=self.num_rows, num_cols=self.num_cols)
        
        for row in self.matrix:
            for col in self.matrix[row]:
                result.set_element(row, col, self.get_element(row, col) - other.get_element(row, col))
        
        for row in other.matrix:
            for col in other.matrix[row]:
                if (row not in self.matrix) or (col not in self.matrix[row]):
                    result.set_element(row, col, -other.get_element(row, col))
        
        return result

    def multiply(self, other):
        if self.num_cols != other.num_rows:
            raise ValueError("Matrices dimensions do not match for multiplication")
        
        result = SparseMatrix(num_rows=self.num_rows, num_cols=other.num_cols)
        
        for row in self.matrix:
            for col in self.matrix[row]:
                for k in range(other.num_cols):
                    result.set_element(row, k, result.get_element(row, k) + self.get_element(row, col) * other.get_element(col, k))
        
        return result
