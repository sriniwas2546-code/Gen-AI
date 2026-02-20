import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        name = entry_name.get()
        age = int(entry_age.get())
        weight = float(entry_weight.get())
        height = float(entry_height.get())

        height_m = height / 100
        bmi = weight / (height_m ** 2)

        # BMI Status
        if bmi < 18.5:
            status = "Underweight"
        elif bmi < 25:
            status = "Normal"
        elif bmi < 30:
            status = "Overweight"
        else:
            status = "Obese"

        # Goal
        goal = goal_var.get()
        base_calories = weight * 30

        if goal == "Weight Gain":
            calories = base_calories + 500
        elif goal == "Weight Loss":
            calories = base_calories - 500
        else:
            calories = base_calories

        # Diet Suggestion
        if status == "Underweight":
            diet = "High Protein Diet\nMilk, Eggs, Paneer"
            workout = "Strength Training\nPushups, Squats"
        elif status == "Normal":
            diet = "Balanced Diet\nRoti, Dal, Fruits"
            workout = "Yoga & Walking"
        elif status == "Overweight":
            diet = "Low Carb Diet\nOats, Salad"
            workout = "Running & Skipping"
        else:
            diet = "Strict Fat Loss Diet\nBoiled Veggies"
            workout = "HIIT & Cardio"

        result_text.set(
            f"Hello {name}\n\n"
            f"BMI: {round(bmi,2)} ({status})\n"
            f"Daily Calories: {int(calories)} kcal\n\n"
            f"Diet:\n{diet}\n\n"
            f"Workout:\n{workout}"
        )

    except:
        messagebox.showerror("Error", "Please enter valid details")


# Main Window
root = tk.Tk()
root.title("Personal Health Coach")
root.geometry("500x600")
root.config(bg="#f0f8ff")

title = tk.Label(root, text="Personal Health Coach",
                 font=("Arial", 18, "bold"),
                 bg="#f0f8ff", fg="#2e8b57")
title.pack(pady=10)

# Input Fields
tk.Label(root, text="Name", bg="#f0f8ff").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Age", bg="#f0f8ff").pack()
entry_age = tk.Entry(root)
entry_age.pack()

tk.Label(root, text="Weight (kg)", bg="#f0f8ff").pack()
entry_weight = tk.Entry(root)
entry_weight.pack()

tk.Label(root, text="Height (cm)", bg="#f0f8ff").pack()
entry_height = tk.Entry(root)
entry_height.pack()

# Goal Dropdown
goal_var = tk.StringVar()
goal_var.set("Maintain Weight")

tk.Label(root, text="Select Goal", bg="#f0f8ff").pack()
goal_menu = tk.OptionMenu(root, goal_var,
                           "Weight Gain",
                           "Maintain Weight",
                           "Weight Loss")
goal_menu.pack()

# Button
tk.Button(root, text="Calculate",
          command=calculate,
          bg="#2e8b57",
          fg="white",
          font=("Arial", 12, "bold")).pack(pady=15)

# Result Area
result_text = tk.StringVar()
tk.Label(root, textvariable=result_text,
         bg="#f0f8ff",
         fg="#00008b",
         justify="left",
         font=("Arial", 11)).pack(pady=10)

root.mainloop()