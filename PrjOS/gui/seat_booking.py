import tkinter as tk
from tkinter import messagebox
from utils.file_handler import read_json
from config.settings import SEATS_FILE
from gui.payment_screen import show_payment_screen
from gui.select_time import show_time_selection

"""
This module provides the functionality for seat booking in a movie ticket booking application.
It uses the Tkinter library to create a graphical user interface for selecting and managing seats.
Functions:
---------
show_seat_booking(root, username, movie_title):
    Displays the seat booking screen where users can select or cancel seats for a specific movie.
    Handles seat selection, cancellation, and navigation to payment or time selection screens.
Parameters:
-----------
root : tk.Tk
    The root Tkinter window where the GUI will be displayed.
username : str
    The username of the user booking the seats.
movie_title : str
    The title of the movie for which seats are being booked.
Dependencies:
-------------
- tkinter: Used for GUI creation.
- utils.file_handler.read_json: Reads JSON data from files.
- config.settings.SEATS_FILE: Path to the JSON file containing seat booking data.
- gui.payment_screen.show_payment_screen: Navigates to the payment screen.
- gui.select_time.show_time_selection: Navigates to the time selection screen.
Features:
---------
- Displays available and booked seats in a grid layout.
- Allows users to select seats to book or cancel their previously booked seats.
- Updates seat status dynamically every second to reflect real-time changes.
- Provides navigation buttons for payment, cancellation, and going back to the previous screen.
Notes:
------
- Seats booked by other users are disabled and displayed in gray.
- Seats booked by the current user are displayed in red and can be canceled.
- Newly selected seats are displayed in light green.
- Seats selected for cancellation are displayed in orange.
"""


def show_seat_booking(root, username, movie_title):
    for widget in root.winfo_children():
        widget.destroy()

    root.geometry("800x600")

    booking_key = f"{movie_title}"
    seat_data = read_json(SEATS_FILE)
    booked_seats = seat_data.get(booking_key, {})

    selected_seats = set()
    selected_to_cancel = set()
    update_id = None

    main_frame = tk.Frame(root)
    main_frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(
        main_frame, text=f"{username}, select your seat for:", font=("Arial", 14)
    ).pack()
    tk.Label(main_frame, text=movie_title, font=("Arial", 14, "bold")).pack(
        pady=(0, 10)
    )

    seat_frame = tk.Frame(main_frame)
    seat_frame.pack()

    buttons = {}

    def toggle_seat(seat_id):
        if seat_id in selected_seats:
            selected_seats.remove(seat_id)
            buttons[seat_id].config(bg="SystemButtonFace")
        elif seat_id in selected_to_cancel:
            selected_to_cancel.remove(seat_id)
            buttons[seat_id].config(bg="red")
        else:
            if seat_id in booked_seats and booked_seats[seat_id] == username:
                selected_to_cancel.add(seat_id)
                buttons[seat_id].config(bg="orange")
            elif seat_id not in booked_seats:
                selected_seats.add(seat_id)
                buttons[seat_id].config(bg="lightgreen")

    # Tạo nút ghế
    for i in range(5):
        for j in range(5):
            seat_id = f"{chr(65 + i)}{j + 1}"
            btn = tk.Button(seat_frame, text=seat_id, width=4)
            btn.grid(row=i, column=j, padx=5, pady=5)
            buttons[seat_id] = btn

            if seat_id in booked_seats:
                if booked_seats[seat_id] == username:
                    btn.config(
                        bg="red",
                        state="normal",
                        command=lambda s=seat_id: toggle_seat(s),
                    )
                else:
                    btn.config(bg="gray", state="disabled")
            else:
                btn.config(command=lambda s=seat_id: toggle_seat(s))

    def update_seat_status():
        nonlocal update_id
        updated_data = read_json(SEATS_FILE)
        updated_booked = updated_data.get(booking_key, {})

        for seat_id, btn in buttons.items():
            if seat_id in selected_seats or seat_id in selected_to_cancel:
                continue

            if seat_id in updated_booked:
                if updated_booked[seat_id] == username:
                    btn.config(
                        bg="red",
                        state="normal",
                        command=lambda s=seat_id: toggle_seat(s),
                    )
                else:
                    btn.config(bg="gray", state="disabled")
            else:
                btn.config(
                    bg="SystemButtonFace",
                    state="normal",
                    command=lambda s=seat_id: toggle_seat(s),
                )

        booked_seats.clear()
        booked_seats.update(updated_booked)

        update_id = root.after(1000, update_seat_status)

    update_seat_status()

    def go_back():
        if update_id:
            root.after_cancel(update_id)
        show_time_selection(root, username, movie_title.split(" - ")[0])

    btn_frame = tk.Frame(main_frame)
    btn_frame.pack(pady=10)

    def pay_selected_seats():
        if selected_seats:
            if update_id:
                root.after_cancel(update_id)
            show_payment_screen(root, username, movie_title, list(selected_seats), [])
        else:
            messagebox.showwarning("No Seats", "Please select seats to book.")

    def cancel_selected_seats():
        if selected_to_cancel:
            if update_id:
                root.after_cancel(update_id)
            show_payment_screen(
                root, username, movie_title, [], list(selected_to_cancel)
            )
        else:
            messagebox.showwarning(
                "No Seats", "Please select your booked seats to cancel."
            )

    tk.Button(
        btn_frame, text="Pay", font=("Arial", 12), width=10, command=pay_selected_seats
    ).pack(side="left", padx=10)

    tk.Button(
        btn_frame,
        text="Cancel",
        font=("Arial", 12),
        width=10,
        command=cancel_selected_seats,
    ).pack(side="left", padx=10)

    tk.Button(main_frame, text="Back", font=("Arial", 12), command=go_back).pack(
        pady=10
    )
