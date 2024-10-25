#!/usr/bin/python3
import sys
import signal

# Initialize counters
total_size = 0
status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_stats():
    """Prints the accumulated statistics."""
    print("File size: {}".format(total_size))
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print("{}: {}".format(code, status_counts[code]))

def handle_interrupt(sig, frame):
    """Handles the keyboard interruption (CTRL + C) to print stats."""
    print_stats()
    sys.exit(0)

# Set the signal handler for keyboard interruption
signal.signal(signal.SIGINT, handle_interrupt)

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()

        # Check the line format: IP - [date] "GET /projects/260 HTTP/1.1" status_code file_size
        if len(parts) < 7:
            continue

        try:
            # Extract and process file size and status code
            status_code = int(parts[-2])
            file_size = int(parts[-1])

            # Update total file size
            total_size += file_size

            # Update status code count if it's one of the specified codes
            if status_code in status_counts:
                status_counts[status_code] += 1

        except (ValueError, IndexError):
            # Ignore lines with invalid data
            continue

        # Print stats every 10 lines
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    # If interrupted, print the stats
    print_stats()
    sys.exit(0)
