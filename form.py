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


# Register form
def register():
    name = full_name.get()
    user_email = email.get()
    user_phone = phone.get()
    user_username = username.get()
    user_password = password.get()
    user_comfirm_password = comfirm_password.get()

    if not name or not user_email or not user_phone or not user_username:
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    if not user_password:
        messagebox.showerror("Error", "Please enter a password")
        return
    if user_password != user_comfirm_password:
        messagebox.showerror(
            "Error",
            "Password and comfirm password do not match."
        )
        return


    messagebox.showinfo(
        "success",
        "Registration succesful!"
    )


# Register button
register_button = tk.Button(
    window,
    text="Register",
    command=register,
    width=20,
    height=2
)
register_button.pack(pady=25)

# run application
window.mainloop()