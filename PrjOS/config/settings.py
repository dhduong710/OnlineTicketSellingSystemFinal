import os

"""
settings.py

This module defines configuration settings and file paths for the project.

Attributes:
    BASE_DIR (str): The base directory of the project, determined dynamically.
    USERS_FILE (str): Path to the JSON file containing user data.
    MOVIES_FILE (str): Path to the JSON file containing movie data.
    SHOWTIMES_FILE (str): Path to the JSON file containing showtime data.
    SEATS_FILE (str): Path to the JSON file containing seat data.
"""

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

USERS_FILE = os.path.join(BASE_DIR, 'data', 'users.json')
MOVIES_FILE = os.path.join(BASE_DIR, 'data', 'movies.json')
SHOWTIMES_FILE = os.path.join(BASE_DIR, 'data', 'showtimes.json')
SEATS_FILE = os.path.join(BASE_DIR, 'data', 'seats.json')

