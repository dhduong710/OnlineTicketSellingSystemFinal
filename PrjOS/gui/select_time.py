# def show_time_selection(root, username, movie_title):
#     """
#     This module provides a function to display a time selection interface for a movie.
#     Functions:
#     ----------
#     show_time_selection(root, username, movie_title):
#         Displays a GUI for selecting a showtime for the given movie. 
#         Clears the current GUI window and populates it with showtime options 
#         retrieved from a JSON file. Allows the user to proceed to seat booking 
#         or navigate back to the movie selection screen.
#     Parameters:
#     -----------
#     root : tkinter.Tk
#         The root tkinter window where the GUI elements will be displayed.
#     username : str
#         The username of the current user.
#     movie_title : str
#         The title of the movie for which showtimes are being selected.
#     Dependencies:
#     -------------
#     - tkinter: Used for GUI components.
#     - gui.seat_booking.show_seat_booking: Navigates to the seat booking interface.
#     - gui.movie_selection.show_movie_selection: Navigates back to the movie selection interface.
#     - utils.file_handler.read_json: Reads JSON data from the specified file.
#     - config.settings.SHOWTIMES_FILE: Path to the JSON file containing showtime data.
#     """
#     import tkinter as tk
#     from gui.seat_booking import show_seat_booking
#     from gui.movie_selection import show_movie_selection
#     from utils.file_handler import read_json
#     from config.settings import SHOWTIMES_FILE  

#     for widget in root.winfo_children():
#         widget.destroy()
#     root.geometry("800x600") 

#     tk.Label(root, text=f"{movie_title}", font=("Arial", 18, "bold")).pack(pady=20)
#     tk.Label(root, text="Select a showtime", font=("Arial", 14)).pack(pady=10)

#     all_times = read_json(SHOWTIMES_FILE)
#     times = all_times.get(movie_title, [])


#     def select_time(time_str):
#         show_seat_booking(root, username, f"{movie_title} - {time_str}")

#     for t in times:
#         tk.Button(root, text=t, width=20, height=2, font=("Arial", 12),
#                   command=lambda x=t: select_time(x)).pack(pady=10)

#     tk.Button(root, text="Back", font=("Arial", 12),
#               command=lambda: show_movie_selection(root, username)).pack(pady=20)

def show_time_selection(root, username, movie_title):
    """
    Attractive showtime selection screen.
    """
    import tkinter as tk
    from gui.seat_booking import show_seat_booking
    from gui.movie_selection import show_movie_selection
    from utils.file_handler import read_json
    from config.settings import SHOWTIMES_FILE  

    for widget in root.winfo_children():
        widget.destroy()
    root.geometry("800x600")
    root.configure(bg="#222831")

    # Header
    tk.Label(
        root, text=movie_title, font=("Arial", 22, "bold"),
        fg="#FFD369", bg="#222831"
    ).pack(pady=(32, 8))
    tk.Label(
        root, text="Select a Showtime", font=("Arial", 15, "bold"),
        fg="#EEEEEE", bg="#222831"
    ).pack(pady=(0, 18))

    all_times = read_json(SHOWTIMES_FILE)
    times = all_times.get(movie_title, [])

    # Showtime buttons frame
    btn_frame = tk.Frame(root, bg="#222831")
    btn_frame.pack(pady=10)

    def select_time(time_str):
        show_seat_booking(root, username, f"{movie_title} - {time_str}")

    def on_enter(e):
        e.widget.config(bg="#FFD369", fg="#222831")
    def on_leave(e):
        e.widget.config(bg="#393E46", fg="#FFD369")

    # Showtimes as attractive buttons
    for t in times:
        btn = tk.Button(
            btn_frame, text=t, width=20, height=2, font=("Arial", 13, "bold"),
            bg="#393E46", fg="#FFD369", activebackground="#FFD369", activeforeground="#222831",
            relief="ridge", bd=2, cursor="hand2",
            command=lambda x=t: select_time(x)
        )
        btn.pack(pady=12)
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)

    # Back button
    def back_on_enter(e):
        e.widget.config(bg="#FFD369", fg="#222831")
    def back_on_leave(e):
        e.widget.config(bg="#222831", fg="#FFD369")

    back_btn = tk.Button(
        root, text="Back", font=("Arial", 12, "bold"),
        bg="#222831", fg="#FFD369", activebackground="#FFD369", activeforeground="#222831",
        relief="ridge", bd=2, cursor="hand2",
        command=lambda: show_movie_selection(root, username)
    )
    back_btn.pack(pady=28, ipadx=12, ipady=4)
    back_btn.bind("<Enter>", back_on_enter)
    back_btn.bind("<Leave>", back_on_leave)