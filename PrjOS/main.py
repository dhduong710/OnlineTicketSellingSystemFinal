import tkinter as tk
"""
This script initializes and runs the main application window for the Online Ticket Selling System.
It uses the tkinter library to create the GUI and imports the `show_login_screen` function 
from the `gui.login_screen` module to display the login screen.
Modules:
    tkinter: Provides tools for creating GUI applications in Python.
    gui.login_screen: Contains the `show_login_screen` function to display the login screen.
Usage:
    Run this script directly to start the application.
"""
from gui.login_screen import show_login_screen

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")  
    root.title("Online Ticket Selling System")
    show_login_screen(root)
    root.mainloop()
    
