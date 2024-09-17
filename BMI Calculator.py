import tkinter as tk

def calculate_bmi():
    """Calculates BMI based on weight and height."""
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        bmi = weight / (height ** 2)
        result_label.config(text=f"BMI: {bmi:.2f}")

        if bmi < 18.5:
            category_label.config(text="Underweight")
        elif 18.5 <= bmi <= 24.9:
            category_label.config(text="Normal weight")
        elif 25 <= bmi <= 29.9:
            category_label.config(text="Overweight")
        else:
            category_label.config(text="Obese")
    except ValueError:
        result_label.config(text="Invalid input. Please enter numbers.")

# Create the main window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("300x200")

# Create labels and entry fields
weight_label = tk.Label(root, text="Weight (kg):")
weight_label.grid(row=0, column=0, padx=5, pady=5)
weight_entry = tk.Entry(root)
weight_entry.grid(row=0, column=1, padx=5, pady=5)

height_label = tk.Label(root, text="Height (m):")
height_label.grid(row=1, column=0, padx=5, pady=5)
height_entry = tk.Entry(root)
height_entry.grid(row=1, column=1, padx=5, pady=5)

calculate_button = tk.Button(root, text="Calculate", command=calculate_bmi)
calculate_button.grid(row=2, columnspan=2, padx=5, pady=5)

result_label = tk.Label(root, text="")
result_label.grid(row=3, columnspan=2, padx=5, pady=5)

category_label = tk.Label(root, text="")
category_label.grid(row=4, columnspan=2, padx=5, pady=5)

# Start the GUI
root.mainloop()