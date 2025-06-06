import json

"""
FILE: file_handler.py
DESCRIPTION:
This module provides utility functions for handling JSON files with file locking
to ensure safe concurrent access. It includes functions for reading and writing
JSON data, as well as a specialized function for safely writing seat data.

FUNCTIONS:
- read_json(filename):
    Reads JSON data from a file with shared lock to prevent write access during
    the read operation.

- write_json(filename, data):
    Writes JSON data to a file with exclusive lock to prevent other processes
    from accessing the file during the write operation.

- safe_write_seats(data, filename="PrjOS/data/seats.json"):
    Writes seat data to a JSON file with exclusive lock, ensuring safe concurrent
    access. Defaults to "PrjOS/data/seats.json" as the target file.

DEPENDENCIES:
- json: Standard library for JSON serialization and deserialization.
- portalocker: Third-party library for file locking to ensure safe concurrent
  file access.
"""
import portalocker


def read_json(filename):
    with open(filename, "r") as f:
        portalocker.lock(f, portalocker.LOCK_SH)
        data = json.load(f)
        portalocker.unlock(f)
        return data


def write_json(filename, data):
    with open(filename, "w") as f:
        portalocker.lock(f, portalocker.LOCK_EX)
        json.dump(data, f, indent=4)
        portalocker.unlock(f)


def safe_write_seats(data, filename="PrjOS/data/seats.json"):
    with open(filename, "w") as f:
        portalocker.lock(f, portalocker.LOCK_EX)
        json.dump(data, f, indent=4)
        portalocker.unlock(f)
