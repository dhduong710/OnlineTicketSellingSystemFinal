import threading
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
"""
from utils.file_handler import read_json, write_json
from config.settings import SEATS_FILE

lock = threading.Lock()

def book_seat(show_id, seat_id, username):
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

def cancel_seat(show_id, seat_id, username):
    with lock:
        data = read_json(SEATS_FILE)
        if show_id in data and data[show_id].get(seat_id) == username:
            del data[show_id][seat_id]
            write_json(SEATS_FILE, data)
            return True
        else:
            return False

