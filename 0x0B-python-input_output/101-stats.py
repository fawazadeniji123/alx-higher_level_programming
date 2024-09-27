#!/usr/bin/python3
"""
reads stdin line by line and computes metrics
"""


import sys


# Initialize variables
total_size = 0
status_codes_count = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0,
}
line_count = 0


def print_metrics():
    """Print the total file size and the status code counts."""
    print(f"File size: {total_size}")
    for code in sorted(status_codes_count.keys()):
        if status_codes_count[code] > 0:
            print(f"{code}: {status_codes_count[code]}")


try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()

        # Extract status code and file size from the log line
        try:
            status_code = parts[-2]
            file_size = int(parts[-1])

            # Update total file size
            total_size += file_size

            # Update status code count if it is one of the expected ones
            if status_code in status_codes_count:
                status_codes_count[status_code] += 1

        except (IndexError, ValueError):
            # If there is an error parsing the line, skip it
            continue

        # Print metrics every 10 lines
        if line_count % 10 == 0:
            print_metrics()

except KeyboardInterrupt:
    # Handle Ctrl+C interruption
    print_metrics()
    sys.exit()

# Print final metrics after EOF
print_metrics()
