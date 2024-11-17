import tkinter as tk
from tkinter import messagebox, ttk
import pandas as pd
import Read

def update_laptop_record(model_name):
    window = tk.Tk()
    window.title("Update Laptop Record")
    window.geometry("600x700")

    try:
        df = pd.read_csv( "project_python/laptop_price - dataset.csv")
    except FileNotFoundError:
        messagebox.showerror("Error", "Dataset file not found.")
        window.destroy()
        return

    if model_name not in df['Product'].values:
        messagebox.showerror("Error", f"Model '{model_name}' not found in the dataset.")
        window.destroy()
        return

    index = df[df['Product'] == model_name].index[0]

    fields = ['Company', 'TypeName', 'Inches', 'ScreenResolution', 'CPU_Company', 'CPU_Type',
              'CPU_Frequency (GHz)', 'RAM (GB)', 'Memory', 'GPU_Company', 'GPU_Type',
              'OpSys', 'Weight (kg)', 'Price (Euro)']
    entries = {}

    tk.Label(window, text=f"Update data for '{model_name}'", font=("Arial", 16, "bold")).pack(pady=10)

    for field in fields:
        tk.Label(window, text=f"{field}:", font=("Arial", 10)).pack(pady=5)
        entry = tk.Entry(window, font=("Arial", 10))
        entry.insert(0, str(df.at[index, field]))
        entry.pack(fill="x", padx=10)
        entries[field] = entry

    def save_changes():
        for field in fields:
            new_value = entries[field].get()
            if field in ['Inches', 'CPU_Frequency (GHz)', 'RAM (GB)', 'Weight (kg)', 'Price (Euro)']:
                df.at[index, field] = float(new_value)
            else:
                df.at[index, field] = new_value

        price = df.at[index, 'Price (Euro)']
        ram = df.at[index, 'RAM (GB)']
        inches = df.at[index, 'Inches']
        weight = df.at[index, 'Weight (kg)']

        df.at[index, 'Price_per_GB_RAM'] = round(price / ram, 2) if ram > 0 else 0
        df.at[index, 'Price_per_Inch'] = round(price / inches, 2) if inches > 0 else 0
        df.at[index, 'Performance_Index'] = round((df.at[index, 'CPU_Frequency (GHz)'] * ram) / weight, 2) if weight > 0 else 0

        df.to_csv( "project_python/laptop_price - dataset.csv", index=False)
        messagebox.showinfo("Success", f"Data for model '{model_name}' has been updated successfully.")
        window.destroy()

    tk.Button(window, text="Update", command=save_changes, font=("Arial", 12, "bold"), bg="#2E7D32", fg="white").pack(pady=20, padx=10, fill="x")

    window.mainloop()