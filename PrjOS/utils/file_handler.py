import json
"""

This module provides utility functions for handling JSON files with thread-safe operations.

Functions:
---------
- read_json(filename):
    Reads a JSON file and returns its content as a Python object.

- write_json(filename, data):
    Writes a Python object to a JSON file with indentation for readability.

- safe_write_seats(data, filename="PrjOS/data/seats.json"):
    Thread-safe function to write seat data to a JSON file.
"""

from threading import Lock

lock = Lock()

def read_json(filename):
    with open(filename, 'r') as f:
        return json.load(f)

def write_json(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def safe_write_seats(data, filename="PrjOS/data/seats.json"):
    with lock:
        with open(filename, 'w') as f:
            json.dump(data, f)

