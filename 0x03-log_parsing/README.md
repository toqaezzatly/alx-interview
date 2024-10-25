
# Log Parsing

This project contains a Python script that reads input logs line by line from stdin, processes them, and computes metrics. The metrics include the total file size and the number of lines for specific HTTP status codes (200, 301, 400, 401, 403, 404, 405, 500). The script prints the accumulated statistics every 10 lines or on keyboard interruption (CTRL + C).

## Requirements
- Python 3
- The script follows the **pycodestyle** style guide.

## Usage

The script reads from `stdin` and prints metrics to `stdout`. You can use the `0-generator.py` script to simulate log input.

### Example

1. Run the generator script:
    ```bash
    ./0-generator.py | ./0-stats.py
    ```

2. After every 10 lines, the script will output the following statistics:
    ```
    File size: <total_size>
    <status_code>: <number_of_occurrences>
    ```
    Example output:
    ```
    File size: 11320
    200: 3
    301: 2
    400: 1
    401: 2
    403: 3
    404: 4
    405: 2
    500: 3
    ```

3. You can stop the script at any time using **CTRL + C**, and it will print the statistics up to that point.

### Input Format

The script expects each log line to be in the following format:
```
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status_code> <file_size>
```

### Handling Input

- If a line does not match the expected format, it will be skipped.
- The status codes must be one of the following: 200, 301, 400, 401, 403, 404, 405, 500.
- The `<file_size>` and `<status_code>` must be integers.

## Files

- **0-stats.py**: The main script that reads logs from `stdin`, processes them, and prints metrics.
- **0-generator.py**: A script to generate random logs for testing purposes.

## Example Workflow

1. Make the scripts executable:
    ```bash
    chmod +x 0-generator.py 0-stats.py
    ```

2. Run the generator and pipe its output to the stats script:
    ```bash
    ./0-generator.py | ./0-stats.py
    ```