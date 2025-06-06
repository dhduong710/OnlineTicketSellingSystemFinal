def show_payment_screen(root, username, movie_title, seat_ids, seats_to_cancel):
    """
    This module provides the `show_payment_screen` function to display a payment screen for booking or canceling movie seats.
    Functions:
    ----------
    - show_payment_screen(root, username, movie_title, seat_ids, seats_to_cancel):
        Displays the payment screen for the user to book or cancel seats for a specific movie.
    Parameters:
    -----------
    - root (tk.Tk): The root Tkinter window where the payment screen will be displayed.
    - username (str): The username of the user performing the booking or cancellation.
    - movie_title (str): The title of the movie for which seats are being booked or canceled.
    - seat_ids (list of str): A list of seat IDs that the user wants to book.
    - seats_to_cancel (list of str): A list of seat IDs that the user wants to cancel.
    Description:
    ------------
    The function clears the current content of the root window and sets up a new payment screen. It provides options for:
    - Booking seats: If `seat_ids` is provided, the user can pay for the selected seats.
    - Canceling seats: If `seats_to_cancel` is provided, the user can cancel the selected seats.
    - Going back: The user can navigate back to the seat booking screen.
    The function uses the `book_seat` and `cancel_seat` functions from the `core.booking_manager` module to handle seat booking and cancellation logic. It also uses the `show_seat_booking` function from the `gui.seat_booking` module to navigate back to the seat booking screen.
    UI Elements:
    ------------
    - Labels to display user information, movie title, and selected seats for booking or cancellation.
    - Buttons for booking seats, canceling seats, and navigating back to the seat booking screen.
    """
    import tkinter as tk
    from tkinter import messagebox
    from gui.seat_booking import show_seat_booking
    from core.booking_manager import book_seat, cancel_seat

    for widget in root.winfo_children():
        widget.destroy()
    root.geometry("800x600")

    def pay_seats():
        booked = []
        failed = []

        for seat_id in seat_ids:
            result = book_seat(movie_title, seat_id, username)
            if result:
                booked.append(seat_id)
            else:
                failed.append(seat_id)

        if booked:
            messagebox.showinfo("Payment Successful", f"Successfully booked seats: {', '.join(booked)}")

        if failed:
            messagebox.showwarning("Some Seats Unavailable", f"The following seats are already booked: {', '.join(failed)}")

        show_seat_booking(root, username, movie_title)

    def cancel_seats():
        cancelled = []
        failed = []
        for seat_id in seats_to_cancel:
            result = cancel_seat(movie_title, seat_id, username)
            if result:
                cancelled.append(seat_id)
            else:
                failed.append(seat_id)

        if cancelled:
            messagebox.showinfo("Cancel Successful", f"Cancelled seats: {', '.join(cancelled)}")
        if failed:
            messagebox.showwarning("Cancel Failed", f"Failed to cancel (not owned or not booked): {', '.join(failed)}")

        show_seat_booking(root, username, movie_title)

    def go_back():
        show_seat_booking(root, username, movie_title)

    tk.Label(root, text=f"User: {username}", font=("Arial", 14)).pack(pady=10)
    tk.Label(root, text=f"Movie: {movie_title}", font=("Arial", 14)).pack(pady=10)
    tk.Label(root, text=f"Seats to Book: {', '.join(seat_ids) if seat_ids else 'None'}", font=("Arial", 14)).pack(pady=10)
    tk.Label(root, text=f"Seats to Cancel: {', '.join(seats_to_cancel) if seats_to_cancel else 'None'}", font=("Arial", 14)).pack(pady=10)

    if seat_ids:
        tk.Button(root, text="Pay for Selected Seats", font=("Arial", 12), bg="green", fg="white", command=pay_seats).pack(pady=10)
    if seats_to_cancel:
        tk.Button(root, text="Cancel Selected Seats", font=("Arial", 12), bg="orange", fg="black", command=cancel_seats).pack(pady=10)

    tk.Button(root, text="Back", font=("Arial", 12), command=go_back).pack(pady=20)
