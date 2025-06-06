
import json
"""
booking_manager.py

This module provides functionality to manage seat bookings for shows. It includes
functions to book a seat and cancel a seat for a specific show. The seat data is
stored in a JSON file, and file locking is used to ensure safe concurrent access.

Functions:
----------
- book_seat(show_id, seat_id, username):
    Attempts to book a seat for a given show. If the seat is already booked, the
    function returns False. Otherwise, it books the seat and returns True.

- cancel_seat(show_id, seat_id, username):
    Cancels a seat booking for a given show if the seat is booked by the specified
    user. Returns True if the cancellation is successful, otherwise returns False.

Dependencies:
-------------
- json: Used for reading and writing seat data in JSON format.
- portalocker: Used for file locking to ensure safe concurrent access.
- config.settings: Contains the SEATS_FILE constant, which specifies the path to
  the JSON file storing seat data.
"""
import portalocker
from config.settings import SEATS_FILE

def book_seat(show_id, seat_id, username):
    with open(SEATS_FILE, 'r+') as f:
        portalocker.lock(f, portalocker.LOCK_EX)
        data = json.load(f)

        if show_id not in data:
            data[show_id] = {}

        if data[show_id].get(seat_id) is None:
            data[show_id][seat_id] = username
            f.seek(0)
            f.truncate()
            json.dump(data, f, indent=4)
            portalocker.unlock(f)
            return True
        else:
            portalocker.unlock(f)
            return False

def cancel_seat(show_id, seat_id, username):
    with open(SEATS_FILE, 'r+') as f:
        portalocker.lock(f, portalocker.LOCK_EX)
        data = json.load(f)

        if show_id in data and data[show_id].get(seat_id) == username:
            del data[show_id][seat_id]
            f.seek(0)
            f.truncate()
            json.dump(data, f, indent=4)
            portalocker.unlock(f)
            return True
        else:
            portalocker.unlock(f)
            return False
