import json
"""
user_manager.py

This module provides functionality for managing user accounts, including user registration and authentication.

Functions:
-----------
- register_user(username: str, password: str) -> bool:
    Registers a new user with the given username and password. 
    Returns False if the username already exists, otherwise adds the user and returns True.

- authenticate_user(username: str, password: str) -> bool:
    Authenticates a user by checking if the provided username and password match an existing user.
    Returns True if authentication is successful, otherwise False.

Dependencies:
-------------
- json: Used for handling JSON data.
- utils.file_handler.read_json: Reads JSON data from a file.
- utils.file_handler.write_json: Writes JSON data to a file.
- config.settings.USERS_FILE: Path to the JSON file storing user data.
"""
from utils.file_handler import read_json, write_json
from config.settings import USERS_FILE

def register_user(username, password):
    users = read_json(USERS_FILE)
    if any(user["username"] == username for user in users):
        return False
    users.append({"username": username, "password": password})
    write_json(USERS_FILE, users)

    return True

def authenticate_user(username, password):
    users = read_json(USERS_FILE)
    return any(user["username"] == username and user["password"] == password for user in users)
