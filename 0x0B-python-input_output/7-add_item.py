#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""


import sys
import os


def main():
    save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
    load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
    # Load existing items from the JSON file if it exists
    items = []
    if os.path.exists('add_item.json'):
        try:
            items = load_from_json_file('add_item.json')
        except Exception:
            # If there's an error loading, just initialize an empty list
            items = []

    # Add command-line arguments (ignoring the script name)
    items.extend(sys.argv[1:])

    # Save the updated list back to the JSON file
    save_to_json_file(items, 'add_item.json')

if __name__ == "__main__":
    main()
