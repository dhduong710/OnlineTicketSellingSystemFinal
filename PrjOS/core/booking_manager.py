import threading
import os
from utils.file_handler import read_json, write_json
from config.settings import SEATS_FILE

"""
This module provides functionality to manage seat bookings for shows. It includes
functions to book a seat and cancel a seat, ensuring thread safety using a lock.

Functions:
    book_seat(show_id, seat_id, username):
        Attempts to book a seat for a specific show. If the seat is already booked,
        the function returns False. Otherwise, it books the seat and returns True.

    cancel_seat(show_id, seat_id, username):
        Cancels a seat booking for a specific show if the seat is booked by the
        specified user. Returns True if the cancellation is successful, otherwise False.

Dependencies:
    - utils.file_handler: Provides `read_json` and `write_json` functions for reading
      and writing JSON data.
    - config.settings: Provides the `SEATS_FILE` constant, which specifies the path
      to the JSON file storing seat booking data.

Thread Safety:
    A threading lock is used to ensure that seat booking and cancellation operations
    are thread-safe.
    A file lock is used to ensure safety across multiple processes.
"""


lock = threading.Lock()


class FileLock:
    """Simple cross-process file lock using a lock file."""

    def __init__(self, filename):
        self.lockfile = filename + ".lock"

    def acquire(self):
        while True:
            try:
                # O_CREAT | O_EXCL ensures atomic creation, fails if file exists
                self.fd = os.open(self.lockfile, os.O_CREAT | os.O_EXCL | os.O_RDWR)
                break
            except FileExistsError:
                pass  # Wait and retry
        # Optionally, write PID or info to lock file

    def release(self):
        try:
            os.close(self.fd)
            os.remove(self.lockfile)
        except Exception:
            pass


file_lock = FileLock(SEATS_FILE)


def book_seat(show_id, seat_id, username):
    file_lock.acquire()
    try:
        with lock:
            data = read_json(SEATS_FILE)
            if show_id not in data:
                data[show_id] = {}
            if data[show_id].get(seat_id) is None:
                data[show_id][seat_id] = username
                write_json(SEATS_FILE, data)
                return True
            else:
                return False
    finally:
        file_lock.release()


def cancel_seat(show_id, seat_id, username):
    file_lock.acquire()
    try:
        with lock:
            data = read_json(SEATS_FILE)
            if show_id in data and data[show_id].get(seat_id) == username:
                del data[show_id][seat_id]
                write_json(SEATS_FILE, data)
                return True
            else:
                return False
    finally:
        file_lock.release()
