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
full_name = tk.Entry(window, width=40)
full_name.pack(pady=5)

# Email
tk.Label(window, text="Email").pack(anchor="w", padx=50)
email = tk.Entry(window, width=40)
email.pack(pady=5)

# Phone
tk.Label(window, text="Phone").pack(anchor="w", padx=50)
phone = tk.Entry(window, width=40)
phone.pack(pady=5)

# Username
tk.Label (window, text="Username").pack(anchor="w", padx=50)
username = tk.Entry(window, width=40)
username.pack(pady=5)

# Password
tk.Label(window, text="Password").pack(anchor="w", padx=50)
password = tk.Entry(window, width=40, show="*")
password.pack(pady=5)

# Comfirm Password
tk.Label(window, text="Comfirm Password").pack(anchor="w", padx=50)
comfirm_password = tk.Entry(window, width=40, show="*")
comfirm_password.pack(pady=5)
