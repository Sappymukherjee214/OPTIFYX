import tkinter as tk
from tkinter import ttk

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        bmi = weight / (height ** 2)
        
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 25:
            category = "Normal weight"
        elif 25 <= bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"
        
        result_label.config(text=f"BMI: {bmi:.2f}\nCategory: {category}")
    except ValueError:
        result_label.config(text="Invalid input. Please enter numeric values.")

# Create the main window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("300x400")
root.configure(bg="#e6ffe6")  # Light green background

# Create and pack the title label
title_label = tk.Label(root, text="BMI Calculator", font=("Arial", 16, "bold"), bg="#e6ffe6")
title_label.pack(pady=10)

# Create and pack the input frame
input_frame = tk.Frame(root, bg="#e6ffe6")
input_frame.pack(pady=10)

# Weight input
weight_label = tk.Label(input_frame, text="Weight (kg):", bg="#e6ffe6")
weight_label.grid(row=0, column=0, padx=5, pady=5)
weight_entry = tk.Entry(input_frame)
weight_entry.grid(row=0, column=1, padx=5, pady=5)

# Height input
height_label = tk.Label(input_frame, text="Height (m):", bg="#e6ffe6")
height_label.grid(row=1, column=0, padx=5, pady=5)
height_entry = tk.Entry(input_frame)
height_entry.grid(row=1, column=1, padx=5, pady=5)

# Calculate button
calculate_button = ttk.Button(root, text="Calculate BMI", command=calculate_bmi)
calculate_button.pack(pady=10)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 12), bg="#e6ffe6")
result_label.pack(pady=10)

# Start the GUI event loop
root.mainloop()