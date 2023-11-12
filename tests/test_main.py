import unittest
from matrix_operations import (
    convert_string_to_matrix,
    count_connected_areas,
)


class TestMatrixAreaCount(unittest.TestCase):
    def test_normal_case(self):
        matrix_string = "1,0,1;0,1,0"
        matrix = convert_string_to_matrix(matrix_string)
        self.assertEqual(count_connected_areas(matrix), 3)

    def test_connected_case(self):
        matrix_string = "1,0,1;1,1,0"
        matrix = convert_string_to_matrix(matrix_string)
        self.assertEqual(count_connected_areas(matrix), 2)

    def test_single_area_case(self):
        matrix_string = "1,1,1,0;0,1,0,0"
        matrix = convert_string_to_matrix(matrix_string)
        self.assertEqual(count_connected_areas(matrix), 1)

    def test_empty_string(self):
        matrix_string = ""
        matrix = convert_string_to_matrix(matrix_string)
        self.assertEqual(count_connected_areas(matrix), 0)

    def test_invalid_format(self):
        matrix_string = "1,1,1;0,1"
        matrix = convert_string_to_matrix(matrix_string)
        self.assertIsNone(matrix)

    def test_large_matrix(self):
        matrix_string = ",".join(["1"] * 101) + ";" + ",".join(["1"] * 101)
        matrix = convert_string_to_matrix(matrix_string)
        self.assertIsNone(matrix)

    def test_empty_matrix(self):
        matrix_string = ""
        matrix = convert_string_to_matrix(matrix_string)
        self.assertEqual(count_connected_areas(matrix), 0)

    def test_matrix_with_only_zeros(self):
        matrix_string = "0,0,0;0,0,0;0,0,0"
        matrix = convert_string_to_matrix(matrix_string)
        self.assertEqual(count_connected_areas(matrix), 0)

    def test_inconsistent_row_lengths(self):
        matrix_string = "1,0,1;0,1"
        matrix = convert_string_to_matrix(matrix_string)
        self.assertIsNone(matrix)

    def test_invalid_characters_in_matrix(self):
        matrix_string = "1,0,a;0,1,0"
        matrix = convert_string_to_matrix(matrix_string)
        self.assertIsNone(matrix)

    def test_matrix_with_only_ones(self):
        matrix_string = "1,1;1,1"
        matrix = convert_string_to_matrix(matrix_string)
        self.assertEqual(count_connected_areas(matrix), 1)


# This allows running the tests from the command line
if __name__ == "__main__":
    unittest.main()
