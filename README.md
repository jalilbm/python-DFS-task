# Matrix Area Counter

## Overview

This Python script is designed to count the number of connected areas of '1's in a given matrix. It accepts a string representation of a matrix, converts it into a 2D matrix, and then utilizes depth-first search (DFS) to identify and count connected areas.

## Features

- Input validation for matrix size and format.
- Depth-first search algorithm to identify connected areas.
- Handles various edge cases like empty strings, non-square matrices, and matrices with invalid characters.

## Requirements

- Python 3.x

## Usage

Run the script in a Python environment. Input the matrix as a string where rows are separated by semicolons (`;`) and columns by commas (`,`).

Example:

`python main.py`

Enter the matrix string: `1,0,1;0,1,0`

Number of areas: `3`

## Testing

The `tests` directory contains unit tests for the script. To run the tests, use the following command:

- `python -m unittest discover -s tests`
