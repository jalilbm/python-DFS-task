def convert_string_to_matrix(matrix_string):
    """
    Converts a string representation of a matrix into a 2D list.

    Args:
    matrix_string (str): A string representing the matrix, where ',' separates columns and ';' separates rows.

    Returns:
    list: 2D list representation of the matrix or None if an error occurs.
    """
    if not matrix_string:
        return []
    try:
        # Split the string into rows and then each row into elements, converting each to an integer
        matrix = [
            [int(element) for element in row.split(",")]
            for row in matrix_string.split(";")
        ]

        # Check if all rows are of the same length
        if any(len(row) != len(matrix[0]) for row in matrix):
            raise ValueError("Inconsistent row lengths in the matrix.")

        # Check if the matrix exceeds the 100x100 size limit
        if len(matrix) > 100 or len(matrix[0]) > 100:
            raise ValueError("Matrix size exceeds 100x100 limit.")

        return matrix
    except ValueError as error:
        # Handle any value errors that occur during matrix conversion
        print(f"Error converting string to matrix: {error}")
        return None


def depth_first_search(matrix, row_index, col_index):
    """
    Depth-first search to mark all adjacent '1's as visited.

    Args:
    matrix (list): The 2D list representing the matrix.
    row_index (int): The current row index.
    col_index (int): The current column index.
    """
    # Check for out-of-bounds or if the current cell is '0'
    if (
        row_index < 0
        or row_index >= len(matrix)
        or col_index < 0
        or col_index >= len(matrix[0])
        or matrix[row_index][col_index] == 0
    ):
        return

    # Mark the current cell as visited by setting it to '0'
    matrix[row_index][col_index] = 0
    # Recursively visit all adjacent cells (up, down, left, right)
    depth_first_search(matrix, row_index + 1, col_index)
    depth_first_search(matrix, row_index - 1, col_index)
    depth_first_search(matrix, row_index, col_index + 1)
    depth_first_search(matrix, row_index, col_index - 1)


def count_connected_areas(matrix):
    """
    Counts the number of distinct areas of '1's in the matrix.

    Args:
    matrix (list): The 2D list representing the matrix.

    Returns:
    int: The number of distinct areas.
    """
    if matrix is None:
        return 0

    area_count = 0
    # Iterate through each cell in the matrix
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            # If a '1' is found, perform DFS from that cell and increment the area count
            if matrix[row][col] == 1:
                depth_first_search(matrix, row, col)
                area_count += 1
    return area_count
