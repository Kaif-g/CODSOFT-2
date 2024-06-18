import tkinter as tk
from tkinter import messagebox

def add():
    try:
        result = float(entry_num1.get()) + float(entry_num2.get())
        result_label.config(text="Result: " + str(result))
    except ValueError:
        messagebox.showerror("Error", "Invalid input! Please enter valid numbers.")

def subtract():
    try:
        result = float(entry_num1.get()) - float(entry_num2.get())
        result_label.config(text="Result: " + str(result))
    except ValueError:
        messagebox.showerror("Error", "Invalid input! Please enter valid numbers.")

def multiply():
    try:
        result = float(entry_num1.get()) * float(entry_num2.get())
        result_label.config(text="Result: " + str(result))
    except ValueError:
        messagebox.showerror("Error", "Invalid input! Please enter valid numbers.")

def divide():
    try:
        num2 = float(entry_num2.get())
        if num2 == 0:
            messagebox.showerror("Error", "Cannot divide by zero!")
        else:
            result = float(entry_num1.get()) / num2
            result_label.config(text="Result: " + str(result))
    except ValueError:
        messagebox.showerror("Error", "Invalid input! Please enter valid numbers.")

# Create main window
root = tk.Tk()
root.title("Simple Calculator")

# Create entry widgets
entry_num1 = tk.Entry(root, width=10)
entry_num1.grid(row=0, column=0, padx=5, pady=5)

entry_num2 = tk.Entry(root, width=10)
entry_num2.grid(row=0, column=1, padx=5, pady=5)

# Create operation buttons
add_button = tk.Button(root, text="+", width=5, command=add)
add_button.grid(row=1, column=0, padx=5, pady=5)

subtract_button = tk.Button(root, text="-", width=5, command=subtract)
subtract_button.grid(row=1, column=1, padx=5, pady=5)

multiply_button = tk.Button(root, text="*", width=5, command=multiply)
multiply_button.grid(row=2, column=0, padx=5, pady=5)

divide_button = tk.Button(root, text="/", width=5, command=divide)
divide_button.grid(row=2, column=1, padx=5, pady=5)

# Create a label to display the result
result_label = tk.Label(root, text="Result:")
result_label.grid(row=3, columnspan=2, padx=5, pady=5)

# Start the Tkinter event loop
root.mainloop()
