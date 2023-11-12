# This script takes a string representation of a matrix as input from the user,
# converts it into a 2D matrix, and then counts the number of connected areas of '1's in the matrix.
# It uses depth-first search (DFS) for matrix traversal.


from matrix_operations import (
    convert_string_to_matrix,
    count_connected_areas,
)

try:
    matrix_input = input("Enter the matrix string: ")
    # Converting the string to a matrix
    matrix = convert_string_to_matrix(matrix_input)
    # Count and print the number of areas
    print(f"Number of areas: {count_connected_areas(matrix)}")
except Exception as error:
    # Handle any unexpected errors during execution
    print(f"An error occurred: {error}")
