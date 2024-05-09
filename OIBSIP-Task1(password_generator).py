import tkinter as tk
from tkinter import ttk
import random
import string
import pyperclip

def generate_password(min_length, max_length, use_upper, use_lower, use_numbers, use_symbols):
    characters = ''
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return None

    length = random.randint(min_length, max_length)
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def copy_to_clipboard(password):
    pyperclip.copy(password)

def generate_and_display_password():
    min_length = int(min_length_entry.get())
    max_length = int(max_length_entry.get())
    use_upper = upper_var.get()
    use_lower = lower_var.get()
    use_numbers = numbers_var.get()
    use_symbols = symbols_var.get()

    password = generate_password(min_length, max_length, use_upper, use_lower, use_numbers, use_symbols)
    if password:
        password_display.config(state=tk.NORMAL)
        password_display.delete('1.0', tk.END)
        password_display.insert(tk.END, password)
        password_display.config(state=tk.DISABLED)
        copy_button.config(state=tk.NORMAL)

root = tk.Tk()
root.title("Password Generator")

title_label = tk.Label(root, text="Password Generator", font=("Arial", 16, "bold"), fg="red")
title_label.grid(row=0, column=0, columnspan=2, padx=10, pady=5, sticky="w")

min_length_label = tk.Label(root, text="Minimum Length:", font=("Arial", 12), anchor="w")
min_length_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

min_length_entry = tk.Entry(root, width=10, font=("Arial", 12))
min_length_entry.grid(row=1, column=1, padx=10, pady=5)

max_length_label = tk.Label(root, text="Maximum Length:", font=("Arial", 12), anchor="w")
max_length_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

max_length_entry = tk.Entry(root, width=10, font=("Arial", 12))
max_length_entry.grid(row=2, column=1, padx=10, pady=5)

upper_var = tk.BooleanVar()
upper_check = ttk.Checkbutton(root, text="Include Uppercase", variable=upper_var, onvalue=True, offvalue=False)
upper_check.grid(row=3, column=0, padx=10, pady=5, sticky="w")
upper_check.state(['selected'])

lower_var = tk.BooleanVar()
lower_check = ttk.Checkbutton(root, text="Include Lowercase", variable=lower_var, onvalue=True, offvalue=False)
lower_check.grid(row=4, column=0, padx=10, pady=5, sticky="w")
lower_check.state(['selected'])

numbers_var = tk.BooleanVar()
numbers_check = ttk.Checkbutton(root, text="Include Numbers", variable=numbers_var, onvalue=True, offvalue=False)
numbers_check.grid(row=5, column=0, padx=10, pady=5, sticky="w")
numbers_check.state(['selected'])

symbols_var = tk.BooleanVar()
symbols_check = ttk.Checkbutton(root, text="Include Symbols", variable=symbols_var, onvalue=True, offvalue=False)
symbols_check.grid(row=6, column=0, padx=10, pady=5, sticky="w")
symbols_check.state(['selected'])

generate_button = tk.Button(root, text="Generate Password", command=generate_and_display_password, font=("Arial", 12))
generate_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

password_display = tk.Text(root, height=1, width=30, state=tk.DISABLED, font=("Arial", 14))
password_display.grid(row=8, column=0, columnspan=2, padx=10, pady=5)

copy_button = tk.Button(root, text="Copy to Clipboard", command=lambda: copy_to_clipboard(password_display.get("1.0", tk.END).strip()), state=tk.DISABLED, font=("Arial", 12))
copy_button.grid(row=9, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()
