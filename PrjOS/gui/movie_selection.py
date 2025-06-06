# def show_movie_selection(root, username):
#     """

#     This module provides the `show_movie_selection` function to display a movie selection screen 
#     in a Tkinter GUI application. The screen allows users to view available movies and select 
#     showtimes for a cinema. It also includes navigation options to return to the login screen.

#     Functions:
#         - show_movie_selection(root, username): Displays the movie selection screen with a list 
#           of movies, their images, and options to select showtimes or return to the login screen.

#     Dependencies:
#         - tkinter: Used for GUI components.
#         - PIL (Pillow): Used for image processing and display.
#         - os: Used for file path manipulations.
#         - gui.select_time.show_time_selection: Function to navigate to the showtime selection screen.
#         - gui.login_screen.show_login_screen: Function to navigate back to the login screen.
#         - utils.file_handler.read_json: Utility function to read JSON files.
#         - config.settings.MOVIES_FILE: Path to the JSON file containing movie data.

#     Usage:
#         Call `show_movie_selection(root, username)` with the root Tkinter window and the username 
#         of the logged-in user to display the movie selection screen.
#     """
#     import tkinter as tk
#     from PIL import Image, ImageTk
#     import os
#     from gui.select_time import show_time_selection
#     from gui.login_screen import show_login_screen
#     from utils.file_handler import read_json
#     from config.settings import MOVIES_FILE  

#     ASSETS_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

#     for widget in root.winfo_children():
#         widget.destroy()

#     root.geometry("800x600")
#     tk.Label(root, text=f"Welcome, {username}!", font=("Arial", 18)).pack(pady=10)
#     tk.Label(root, text="Available Movies At HUST Cinema Today", font=("Arial", 14)).pack(pady=5)

#     scroll_frame_container = tk.Frame(root)
#     scroll_frame_container.pack(fill="both", expand=True, padx=10)

#     canvas = tk.Canvas(scroll_frame_container)
#     scrollbar = tk.Scrollbar(scroll_frame_container, orient="vertical", command=canvas.yview)
#     scrollable_frame = tk.Frame(canvas)

#     scrollable_frame.bind(
#         "<Configure>",
#         lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
#     )

#     canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
#     canvas.configure(yscrollcommand=scrollbar.set)

#     canvas.pack(side="left", fill="both", expand=True)
#     scrollbar.pack(side="right", fill="y")

#     def _on_mousewheel(event):
#         canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

#     canvas.bind_all("<MouseWheel>", _on_mousewheel)

#     movies = read_json(MOVIES_FILE)

#     for movie in movies:
#         frame = tk.Frame(scrollable_frame, pady=10)
#         frame.pack(fill="x", padx=20)

#         img_path = os.path.join(ASSETS_DIR, movie["image"])
#         try:
#             img = Image.open(img_path)
#             img = img.resize((150, 220))
#             photo = ImageTk.PhotoImage(img)
#             img_label = tk.Label(frame, image=photo)
#             img_label.image = photo
#             img_label.pack(side="left", padx=10)
#         except:
#             tk.Label(frame, text="[Image Not Found]").pack(side="left", padx=10)

#         info_frame = tk.Frame(frame)
#         info_frame.pack(side="left", fill="x", expand=True, padx=10)

#         tk.Label(info_frame, text=movie["title"], font=("Arial", 14, "bold"), anchor="w").pack(anchor="w")
#         tk.Button(info_frame, text="Select Showtime", font=("Arial", 12),
#                   command=lambda m=movie["title"]: show_time_selection(root, username, m)).pack(anchor="w", pady=10)

#     tk.Button(root, text="Back to Login", font=("Arial", 12),
#               command=lambda: show_login_screen(root)).pack(pady=15)
def show_movie_selection(root, username):
    """
    Improved movie selection UI (fixed image loading).
    """
    import tkinter as tk
    from PIL import Image, ImageTk, ImageOps
    import os
    from gui.select_time import show_time_selection
    from gui.login_screen import show_login_screen
    from utils.file_handler import read_json
    from config.settings import MOVIES_FILE  

    ASSETS_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

    for widget in root.winfo_children():
        widget.destroy()

    root.geometry("900x650")
    root.configure(bg="#222831")

    header = tk.Label(root, text=f"Welcome, {username}!", font=("Arial", 22, "bold"), fg="#FFD369", bg="#222831")
    header.pack(pady=(18, 2))
    subheader = tk.Label(root, text="Available Movies At HUST Cinema Today", font=("Arial", 16, "bold"), fg="#EEEEEE", bg="#222831")
    subheader.pack(pady=(0, 10))

    scroll_frame_container = tk.Frame(root, bg="#222831")
    scroll_frame_container.pack(fill="both", expand=True, padx=18)

    canvas = tk.Canvas(scroll_frame_container, bg="#222831", highlightthickness=0)
    scrollbar = tk.Scrollbar(scroll_frame_container, orient="vertical", command=canvas.yview, bg="#393E46", troughcolor="#393E46")
    scrollable_frame = tk.Frame(canvas, bg="#222831")

    def _on_mousewheel(event):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    canvas.bind_all("<MouseWheel>", _on_mousewheel)

    movies = read_json(MOVIES_FILE)

    def on_enter(e):
        e.widget.config(bg="#FFD369", fg="#222831")
    def on_leave(e):
        e.widget.config(bg="#393E46", fg="#FFD369")

    for movie in movies:
        card = tk.Frame(scrollable_frame, bg="#393E46", bd=2, relief="ridge")
        card.pack(fill="x", padx=10, pady=14, ipadx=6, ipady=6)

        img_path = os.path.join(ASSETS_DIR, movie["image"])
        try:
            # Print for debugging if needed
            # print("Loading image:", img_path)
            img = Image.open(img_path)
            img = ImageOps.fit(img, (120, 180), Image.Resampling.LANCZOS if hasattr(Image, "Resampling") else Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(img)
            img_label = tk.Label(card, image=photo, bg="#393E46")
            img_label.image = photo
            img_label.pack(side="left", padx=12, pady=6)
        except Exception as e:
            # print("Image load error:", e)
            fallback = tk.Label(card, text="[Image Not Found]", width=16, height=10, bg="#393E46", fg="#FFD369", font=("Arial", 10, "italic"))
            fallback.pack(side="left", padx=12, pady=6)

        info_frame = tk.Frame(card, bg="#393E46")
        info_frame.pack(side="left", fill="x", expand=True, padx=10)

        tk.Label(info_frame, text=movie["title"], font=("Arial", 16, "bold"), fg="#FFD369", bg="#393E46", anchor="w").pack(anchor="w", pady=(0, 6))
        if "description" in movie:
            tk.Label(info_frame, text=movie["description"], font=("Arial", 11), fg="#EEEEEE", bg="#393E46", anchor="w", wraplength=500, justify="left").pack(anchor="w", pady=(0, 8))

        btn = tk.Button(
            info_frame, text="Select Showtime", font=("Arial", 12, "bold"),
            bg="#393E46", fg="#FFD369", activebackground="#FFD369", activeforeground="#222831",
            relief="raised", bd=2,
            command=lambda m=movie["title"]: show_time_selection(root, username, m)
        )
        btn.pack(anchor="w", pady=8, ipadx=8, ipady=2)
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)

    back_btn = tk.Button(
        root, text="Back to Login", font=("Arial", 12, "bold"),
        bg="#222831", fg="#FFD369", activebackground="#FFD369", activeforeground="#222831",
        relief="ridge", bd=2,
        command=lambda: show_login_screen(root)
    )
    back_btn.pack(pady=18, ipadx=10, ipady=3)
    back_btn.bind("<Enter>", on_enter)
    back_btn.bind("<Leave>", on_leave)