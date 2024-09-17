import random
import string
import tkinter as tk

def generate_password(length, strength):
    """Generates a random password based on length and strength."""

    characters = ""
    if strength == "Low":
        characters += string.ascii_letters
    elif strength == "Medium":
        characters += string.ascii_letters + string.digits
    else:
        characters += string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def copy_to_clipboard(password):
    """Copies the generated password to the clipboard."""
    root.clipboard_clear()
    root.clipboard_append(password)

def generate_password_and_display():
    """Generates a password and displays it in the text box."""
    length = int(length_var.get())
    strength = strength_var.get()
    password = generate_password(length, strength)
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# Create the main window
root = tk.Tk()
root.title("Random Password Generator")

# Create labels, entry fields, and buttons
password_label = tk.Label(root, text="Password:")
password_label.grid(row=0, column=0, padx=5, pady=5)
password_entry = tk.Entry(root, width=40)
password_entry.grid(row=0, column=1, padx=5, pady=5)

copy_button = tk.Button(root, text="Copy", command=lambda: copy_to_clipboard(password_entry.get()))
copy_button.grid(row=0, column=2, padx=5, pady=5)
generate_button = tk.Button(root, text="Generate", command=generate_password_and_display)
generate_button.grid(row=0, column=3, padx=5, pady=5)

length_label = tk.Label(root, text="Length:")
length_label.grid(row=1, column=0, padx=5, pady=5)
length_var = tk.IntVar()
length_spinbox = tk.Spinbox(root, from_=8, to=32, textvariable=length_var)
length_spinbox.grid(row=1, column=1, padx=5, pady=5)

strength_label = tk.Label(root, text="Strength:")
strength_label.grid(row=1, column=2, padx=5, pady=5)
strength_var = tk.StringVar()
strength_var.set("Medium")
strength_radio_low = tk.Radiobutton(root, text="Low", variable=strength_var, value="Low")
strength_radio_low.grid(row=1, column=3)
strength_radio_medium = tk.Radiobutton(root, text="Medium", variable=strength_var, value="Medium")
strength_radio_medium.grid(row=1, column=4)
strength_radio_strong = tk.Radiobutton(root, text="Strong", variable=strength_var, value="Strong")
strength_radio_strong.grid(row=1, column=5)

# Start the GUI
root.mainloop()