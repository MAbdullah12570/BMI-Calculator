import tkinter as tk
from tkinter import messagebox

def calculate_bmi(weight, height_meters):
    bmi = weight / (height_meters ** 2)
    return bmi

def feet_to_meters(feet):
    return feet * 0.3048

def on_calculate():
    try:
        weight = float(entry_weight.get())
        height_feet = float(entry_height.get())
        height_meters = feet_to_meters(height_feet)
        bmi = calculate_bmi(weight, height_meters)
        result = f"Your BMI is {bmi:.2f}\n"
        if bmi < 18.5:
            result += "You are underweight."
        elif 18.5 <= bmi < 24.9:
            result += "You have a normal weight."
        elif 25 <= bmi < 29.9:
            result += "You are overweight."
        else:
            result += "You are obese."
        messagebox.showinfo("BMI Result", result)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

def toggle_mode():
    if mode.get() == "Dark":
        root.config(bg="black")
        for widget in root.winfo_children():
            widget.config(bg="black", fg="white", font=("Helvetica", 14))
        entry_weight.config(insertbackground="white")
        entry_height.config(insertbackground="white")
    else:
        root.config(bg="white")
        for widget in root.winfo_children():
            widget.config(bg="white", fg="black", font=("Helvetica", 14))
        entry_weight.config(insertbackground="black")
        entry_height.config(insertbackground="black")

# Create the main window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("700x300")  # Set window size

# Create a variable to store the mode
mode = tk.StringVar(value="Light")

# Create and place the widgets
tk.Label(root, text="Enter your weight in kilograms:", font=("Helvetica", 14)).grid(row=0, column=0, padx=10, pady=10)
entry_weight = tk.Entry(root, font=("Helvetica", 14))
entry_weight.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Enter your height in feet:", font=("Helvetica", 14)).grid(row=1, column=0, padx=10, pady=10)
entry_height = tk.Entry(root, font=("Helvetica", 14))
entry_height.grid(row=1, column=1, padx=10, pady=10)

tk.Button(root, text="Calculate BMI", command=on_calculate, font=("Helvetica", 14)).grid(row=2, columnspan=2, pady=10)

# Add a toggle button for dark/light mode
tk.Radiobutton(root, text="Light Mode", variable=mode, value="Light", command=toggle_mode, font=("Helvetica", 14)).grid(row=3, column=0, pady=10)
tk.Radiobutton(root, text="Dark Mode", variable=mode, value="Dark", command=toggle_mode, font=("Helvetica", 14)).grid(row=3, column=1, pady=10)

# Run the application
root.mainloop()
