import tkinter as tk
from tkinter import ttk
import random
import string
import pyperclip

def generate_password():
    length = int(length_var.get())
    strength = strength_var.get()

    if strength == "Low":
        characters = string.ascii_letters + string.digits
    elif strength == "Medium":
        characters = string.ascii_letters + string.digits + string.punctuation
    else:  # Strong
        characters = string.ascii_letters + string.digits + string.punctuation + string.ascii_letters.upper()

    password = ''.join(random.choice(characters) for _ in range(length))
    password_var.set(password)

def copy_password():
    password = password_var.get()
    pyperclip.copy(password)

# Create the main window
root = tk.Tk()
root.title("Random Password Generator")
root.geometry("400x200")
root.configure(bg="#e6f3ff")

# Create and pack the title label
title_label = tk.Label(root, text="Random Password Generator", font=("Arial", 16, "bold"), bg="#e6f3ff")
title_label.pack(pady=10)

# Create the main frame
main_frame = ttk.Frame(root, padding="10")
main_frame.pack(fill=tk.BOTH, expand=True)

# Password display
password_var = tk.StringVar()
password_entry = ttk.Entry(main_frame, textvariable=password_var, width=30)
password_entry.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="w")

# Copy button
copy_button = ttk.Button(main_frame, text="Copy", command=copy_password)
copy_button.grid(row=0, column=2, padx=5, pady=5)

# Generate button
generate_button = ttk.Button(main_frame, text="Generate", command=generate_password)
generate_button.grid(row=0, column=3, padx=5, pady=5)

# Length selection
ttk.Label(main_frame, text="Length:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
length_var = tk.StringVar(value="8")
length_combo = ttk.Combobox(main_frame, textvariable=length_var, values=[str(i) for i in range(8, 33)], width=5)
length_combo.grid(row=1, column=1, padx=5, pady=5, sticky="w")

# Strength selection
strength_var = tk.StringVar(value="Medium")
ttk.Radiobutton(main_frame, text="Low", variable=strength_var, value="Low").grid(row=2, column=0, padx=5, pady=5, sticky="w")
ttk.Radiobutton(main_frame, text="Medium", variable=strength_var, value="Medium").grid(row=2, column=1, padx=5, pady=5, sticky="w")
ttk.Radiobutton(main_frame, text="Strong", variable=strength_var, value="Strong").grid(row=2, column=2, padx=5, pady=5, sticky="w")

# Start the GUI event loop
root.mainloop()