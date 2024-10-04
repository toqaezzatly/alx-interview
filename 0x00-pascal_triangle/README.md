

```markdown
# Pascal's Triangle

This project includes a Python function that generates Pascal's triangle up to a specified number of rows. The triangle is represented as a list of lists, where each inner list contains the integers of that row.

## Table of Contents

- [Requirements](#requirements)
- [Usage](#usage)
- [Functionality](#functionality)
- [Example](#example)
- [Contributing](#contributing)

## Requirements

- Python 3.x





1. Make sure you have Python 3 installed on your system.

## Usage

To use the `pascal_triangle` function, you can either import it into your script or run the provided `0-main.py` file, which demonstrates how to print Pascal's triangle.

### Importing the Function

You can import the function like this:

```python

from pascal_triangle import pascal_triangle

# Example usage
triangle = pascal_triangle(5)
print(triangle)  # Output: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
```

### Running the Example

To see an example in action, run the provided `0-main.py` file:

```bash
python3 0-main.py
```

## Functionality

The `pascal_triangle(n)` function takes a single integer `n` as input and returns a list of lists representing Pascal's triangle with `n` rows. The function behaves as follows:

- If `n <= 0`, it returns an empty list.
- For positive `n`, it constructs the triangle row by row.

## Example

```python
>>> from pascal_triangle import pascal_triangle
>>> print(pascal_triangle(5))
[[1], 
 [1, 1], 
 [1, 2, 1], 
 [1, 3, 3, 1], 
 [1, 4, 6, 4, 1]]
```

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request with your changes. 

