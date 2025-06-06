# def show_login_screen(root):
#     """

#     This module provides the functionality to display a login screen using the Tkinter library. 
#     It includes features for user authentication and registration.

#     Functions:
#     ----------
#     show_login_screen(root):
#         Displays the login screen on the provided Tkinter root window. 
#         Allows users to log in or register a new account.

#         Parameters:
#         - root (tk.Tk): The root Tkinter window where the login screen will be displayed.

#         Features:
#         - Login functionality:
#             - Prompts the user for a username and password.
#             - Authenticates the user using the `authenticate_user` function from `core.user_manager`.
#             - On successful login, navigates to the movie selection screen using `show_movie_selection`.
#             - Displays error messages for invalid credentials.
#         - Registration functionality:
#             - Opens a new window for user registration.
#             - Prompts the user for a new username and password.
#             - Registers the user using the `register_user` function from `core.user_manager`.
#             - Displays success or error messages based on the registration outcome.
#     """
#     import tkinter as tk
#     from tkinter import messagebox
#     from gui.movie_selection import show_movie_selection
#     from core.user_manager import authenticate_user, register_user
#     for widget in root.winfo_children():
#         widget.destroy()
#     root.geometry("800x600")  

#     def login():
#         username = username_entry.get()
#         password = password_entry.get()
#         if authenticate_user(username, password):
#             messagebox.showinfo("Login Success", "Welcome!")
#             show_movie_selection(root, username)
#         else:
#             messagebox.showerror("Login Failed", "Invalid credentials")

#     def open_register_window():
#         register_window = tk.Toplevel(root)
#         register_window.title("Register")
#         register_window.geometry("300x200")

#         tk.Label(register_window, text="New Username").pack(pady=5)
#         new_username_entry = tk.Entry(register_window)
#         new_username_entry.pack(pady=5)

#         tk.Label(register_window, text="New Password").pack(pady=5)
#         new_password_entry = tk.Entry(register_window, show="*")
#         new_password_entry.pack(pady=5)

#         def register():
#             new_username = new_username_entry.get()
#             new_password = new_password_entry.get()
#             if register_user(new_username, new_password):
#                 messagebox.showinfo("Success", "Registration successful!")
#                 register_window.destroy()
#             else:
#                 messagebox.showerror("Error", "Username already exists")

#         tk.Button(register_window, text="Register", command=register).pack(pady=10)

#     tk.Label(root, text="Username").pack(pady=5)
#     username_entry = tk.Entry(root)
#     username_entry.pack(pady=5)

#     tk.Label(root, text="Password").pack(pady=5)
#     password_entry = tk.Entry(root, show="*")
#     password_entry.pack(pady=5)

#     tk.Button(root, text="Login", command=login).pack(pady=10)
#     tk.Button(root, text="Register", command=open_register_window).pack()
def show_login_screen(root):
    """
    Enhanced login screen with modern UI.
    """
    import tkinter as tk
    from tkinter import messagebox
    from gui.movie_selection import show_movie_selection
    from core.user_manager import authenticate_user, register_user

    for widget in root.winfo_children():
        widget.destroy()
    root.geometry("800x600")
    root.configure(bg="#222831")

    # Centered frame for login box
    login_frame = tk.Frame(root, bg="#393E46", bd=2, relief="ridge")
    login_frame.place(relx=0.5, rely=0.5, anchor="center", width=370, height=370)

    tk.Label(
        login_frame, text="🎬 HUST Cinema Login", font=("Arial", 20, "bold"),
        fg="#FFD369", bg="#393E46"
    ).pack(pady=(28, 10))

    tk.Label(login_frame, text="Username", font=("Arial", 12), fg="#EEEEEE", bg="#393E46").pack(pady=(12, 2))
    username_entry = tk.Entry(login_frame, font=("Arial", 12), bg="#EEEEEE", fg="#222831", bd=1, relief="solid")
    username_entry.pack(pady=2, ipadx=6, ipady=4)

    tk.Label(login_frame, text="Password", font=("Arial", 12), fg="#EEEEEE", bg="#393E46").pack(pady=(12, 2))
    password_entry = tk.Entry(login_frame, show="*", font=("Arial", 12), bg="#EEEEEE", fg="#222831", bd=1, relief="solid")
    password_entry.pack(pady=2, ipadx=6, ipady=4)

    def login():
        username = username_entry.get()
        password = password_entry.get()
        if authenticate_user(username, password):
            messagebox.showinfo("Login Success", "Welcome!")
            show_movie_selection(root, username)
        else:
            messagebox.showerror("Login Failed", "Invalid credentials")

    def open_register_window():
        register_window = tk.Toplevel(root)
        register_window.title("Register")
        register_window.geometry("340x280")
        register_window.configure(bg="#393E46")

        tk.Label(register_window, text="Register New Account", font=("Arial", 15, "bold"), fg="#FFD369", bg="#393E46").pack(pady=(18, 8))
        tk.Label(register_window, text="New Username", font=("Arial", 11), fg="#EEEEEE", bg="#393E46").pack(pady=(6, 2))
        new_username_entry = tk.Entry(register_window, font=("Arial", 11), bg="#EEEEEE", fg="#222831", bd=1, relief="solid")
        new_username_entry.pack(pady=2, ipadx=5, ipady=3)

        tk.Label(register_window, text="New Password", font=("Arial", 11), fg="#EEEEEE", bg="#393E46").pack(pady=(10, 2))
        new_password_entry = tk.Entry(register_window, show="*", font=("Arial", 11), bg="#EEEEEE", fg="#222831", bd=1, relief="solid")
        new_password_entry.pack(pady=2, ipadx=5, ipady=3)

        def register():
            new_username = new_username_entry.get()
            new_password = new_password_entry.get()
            if register_user(new_username, new_password):
                messagebox.showinfo("Success", "Registration successful!")
                register_window.destroy()
            else:
                messagebox.showerror("Error", "Username already exists")

        reg_btn = tk.Button(
            register_window, text="Register", font=("Arial", 12, "bold"),
            bg="#FFD369", fg="#222831", activebackground="#222831", activeforeground="#FFD369",
            relief="ridge", bd=2, command=register
        )
        reg_btn.pack(pady=18, ipadx=10, ipady=3)
        reg_btn.bind("<Enter>", lambda e: reg_btn.config(bg="#222831", fg="#FFD369"))
        reg_btn.bind("<Leave>", lambda e: reg_btn.config(bg="#FFD369", fg="#222831"))

    # Button hover effects
    def on_enter(e):
        e.widget.config(bg="#FFD369", fg="#222831")
    def on_leave(e):
        e.widget.config(bg="#222831", fg="#FFD369")

    login_btn = tk.Button(
        login_frame, text="Login", font=("Arial", 13, "bold"),
        bg="#222831", fg="#FFD369", activebackground="#FFD369", activeforeground="#222831",
        relief="ridge", bd=2, command=login
    )
    login_btn.pack(pady=(28, 10), ipadx=12, ipady=4)
    login_btn.bind("<Enter>", on_enter)
    login_btn.bind("<Leave>", on_leave)

    reg_btn = tk.Button(
        login_frame, text="Register", font=("Arial", 12, "bold"),
        bg="#222831", fg="#FFD369", activebackground="#FFD369", activeforeground="#222831",
        relief="ridge", bd=2, command=open_register_window
    )
    reg_btn.pack(ipadx=8, ipady=3)
    reg_btn.bind("<Enter>", on_enter)
    reg_btn.bind("<Leave>", on_leave)