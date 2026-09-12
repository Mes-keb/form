import tkinter as tk
from tkinter import messagebox

# Create window
window = tk.Tk()
window.title("Registration form")
window.geometry("400x450")
window.resizelble(False, False)

# Title
title = tk.Label(
    window,
    text="Registration Form",
    font=("Ariel", 20, "bold")
)
title.pack(pady=20)

# Full name
tk.Label(window, text="Full Name").pack(ancor="w", padx=50)
