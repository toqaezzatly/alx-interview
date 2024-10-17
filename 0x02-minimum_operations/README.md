
# MinOperations Project

## Description

This project contains a Python function that calculates the minimum number of operations required to result in exactly **n** "H" characters in a file, starting with a single "H". The available operations are:
- **Copy All**: Copy all characters in the file.
- **Paste**: Paste the copied characters.

The goal is to achieve exactly **n** characters using the fewest number of operations.

## Function Prototype

```python
def minOperations(n):
    """
    Calculate the minimum number of operations needed to result in exactly n H characters in the file.
    
    Arguments:
    n : int : The target number of H characters.
    
    Returns:
    int : The minimum number of operations required, or 0 if n cannot be achieved.
    """
```

### Parameters:
- **n**: An integer representing the number of "H" characters you want in the file.

### Returns:
- Returns the minimum number of operations needed to achieve exactly **n** "H" characters.
- If it is impossible to achieve exactly **n** "H" characters, the function returns **0**.

## Example

Here is an example illustrating the calculation:

```python
minOperations(9)
```

The operations are:
- H → Copy All → Paste → HH → Paste → HHH → Copy All → Paste → HHHHHH → Paste → HHHHHHHHH

The total number of operations is **6**.

## Usage

### Prerequisites
- Python 3.x must be installed.

### How to Run

1. Clone this repository to your local machine.
2. Open a terminal and navigate to the directory containing the Python file.
3. Run the following command to test the function with different values of **n**.

```bash
python3 0-main.py
```

### Example Output
```bash
$ ./0-main.py
Min number of operations to reach 4 characters: 4
Min number of operations to reach 12 characters: 7
$
```

## Project Files

- `0-main.py`: The main file to test the function with different inputs.
- `0-minoperations.py`: The file that contains the `minOperations()` function.

## Author

- **Your Name**: Toqa Ayman Jumaa

