def show_time_selection(root, username, movie_title):
    """
    This module provides a function to display a time selection interface for a movie.
    Functions:
    ----------
    show_time_selection(root, username, movie_title):
        Displays a GUI for selecting a showtime for the given movie. 
        Clears the current GUI window and populates it with showtime options 
        retrieved from a JSON file. Allows the user to proceed to seat booking 
        or navigate back to the movie selection screen.
    Parameters:
    -----------
    root : tkinter.Tk
        The root tkinter window where the GUI elements will be displayed.
    username : str
        The username of the current user.
    movie_title : str
        The title of the movie for which showtimes are being selected.
    Dependencies:
    -------------
    - tkinter: Used for GUI components.
    - gui.seat_booking.show_seat_booking: Navigates to the seat booking interface.
    - gui.movie_selection.show_movie_selection: Navigates back to the movie selection interface.
    - utils.file_handler.read_json: Reads JSON data from the specified file.
    - config.settings.SHOWTIMES_FILE: Path to the JSON file containing showtime data.
    """
    import tkinter as tk
    from gui.seat_booking import show_seat_booking
    from gui.movie_selection import show_movie_selection
    from utils.file_handler import read_json
    from config.settings import SHOWTIMES_FILE  

    for widget in root.winfo_children():
        widget.destroy()
    root.geometry("800x600") 

    tk.Label(root, text=f"{movie_title}", font=("Arial", 18, "bold")).pack(pady=20)
    tk.Label(root, text="Select a showtime", font=("Arial", 14)).pack(pady=10)

    all_times = read_json(SHOWTIMES_FILE)
    times = all_times.get(movie_title, [])


    def select_time(time_str):
        show_seat_booking(root, username, f"{movie_title} - {time_str}")

    for t in times:
        tk.Button(root, text=t, width=20, height=2, font=("Arial", 12),
                  command=lambda x=t: select_time(x)).pack(pady=10)

    tk.Button(root, text="Back", font=("Arial", 12),
              command=lambda: show_movie_selection(root, username)).pack(pady=20)
