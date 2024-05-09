import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import os

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def calculate_and_display_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if weight <= 0 or height <= 0:
            raise ValueError("Please enter valid weight and height.")

        bmi = calculate_bmi(weight, height)
        category = classify_bmi(bmi)

        result_text = "Your BMI is: {:.2f}\nYou are classified as: {}".format(bmi, category)
        result_label.config(text=result_text)

        # Save data to file
        save_data(weight, height, bmi, category)
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def save_data(weight, height, bmi, category):
    with open("bmi_data.txt", "a") as file:
        file.write("{:.2f}, {:.2f}, {:.2f}, {}\n".format(weight, height, bmi, category))

def plot_bmi_history():
    if not os.path.exists("bmi_data.txt"):
        messagebox.showinfo("Info", "No BMI data found.")
        return

    weights = []
    heights = []
    bmis = []
    categories = []

    with open("bmi_data.txt", "r") as file:
        for line in file:
            data = line.strip().split(", ")
            weights.append(float(data[0]))
            heights.append(float(data[1]))
            bmis.append(float(data[2]))
            categories.append(data[3])

    plt.figure(figsize=(8, 6))
    plt.plot(weights, bmis, marker='o', linestyle='-')
    plt.title("BMI History")
    plt.xlabel("Weight (kg)")
    plt.ylabel("BMI")
    plt.grid(True)
    plt.show()

root = tk.Tk()
root.title("BMI Calculator")
root.geometry("300x300")

# Frame to contain input fields
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

weight_label = tk.Label(input_frame, text="Weight (kg):", font=("Arial", 12))
weight_label.grid(row=0, column=0, padx=5, pady=5)

weight_entry = tk.Entry(input_frame, font=("Arial", 12))
weight_entry.grid(row=0, column=1, padx=5, pady=5)

height_label = tk.Label(input_frame, text="Height (m):", font=("Arial", 12))
height_label.grid(row=1, column=0, padx=5, pady=5)

height_entry = tk.Entry(input_frame, font=("Arial", 12))
height_entry.grid(row=1, column=1, padx=5, pady=5)

calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_and_display_bmi, font=("Arial", 12), bg="green", fg="white")
calculate_button.pack(pady=5)

plot_button = tk.Button(root, text="Plot BMI History", command=plot_bmi_history, font=("Arial", 12))
plot_button.pack(pady=5)

# Frame to contain result label
result_frame = tk.Frame(root)
result_frame.pack(padx=10, pady=10)

result_label = tk.Label(result_frame, text="", font=("Arial", 14), fg="blue")
result_label.pack()

root.mainloop()
