import tkinter as tk
from tkinter import messagebox, ttk
import pandas as pd
import Read

def update_laptop_record(model_name):
    
    # Cập nhật dữ liệu laptop dựa trên model name.
    # Tạo cửa sổ cập nhật dữ liệu
    window = tk.Tk()
    window.title("Cập nhật dữ liệu laptop")
    window.geometry("600x700")
    window.config(bg="#E8F5E9")

    try:
        # Đọc dữ liệu từ file CSV
        df = pd.read_csv("project_python/laptop_price - dataset.csv")
    except FileNotFoundError:
        messagebox.showerror("Lỗi", "Không tìm thấy file CSV.")
        window.destroy()
        return

    # Kiểm tra xem model có tồn tại trong dữ liệu không
    if model_name not in df['Model'].values:
        messagebox.showerror("Lỗi", f"Model '{model_name}' không tồn tại trong dữ liệu.")
        window.destroy()
        return

    # Lấy index của bản ghi cần cập nhật
    index = df[df['Model'] == model_name].index[0]

    # Các trường cần cập nhật
    fields = ['Brand', 'Processor', 'RAM', 'Storage', 'Screen Size', 'Price', 'Operating System', 'Weight']
    entries = {}

    # Tiêu đề
    tk.Label(window, text=f"Cập nhật dữ liệu cho '{model_name}'", font=("Arial", 16, "bold"), bg="#E8F5E9").pack(pady=10)

    # Tạo các ô nhập liệu
    for idx, field in enumerate(fields):
        tk.Label(window, text=f"{field}:", font=("Arial", 10), bg="#E8F5E9").pack(pady=5)
        entry = tk.Entry(window, font=("Arial", 10))
        entry.insert(0, str(df.at[index, field]))  # Điền giá trị hiện tại vào ô nhập liệu
        entry.pack(fill="x", padx=10)
        entries[field] = entry

    # Hàm lưu thay đổi
    def save_changes():
        for field in fields:
            new_value = entries[field].get()
            if field == 'Price':
                df.at[index, field] = float(new_value)
            elif field == 'Weight':
                df.at[index, field] = new_value.strip()
            else:
                df.at[index, field] = new_value

        # Tính toán lại các thông tin bổ sung
        price = df.at[index, 'Price']
        weight = df.at[index, 'Weight']
        df.at[index, 'Price in Thousands'] = round(price / 1000, 2) if price > 0 else 0
        df.at[index, 'Weight Category'] = 'Light' if float(weight.strip('kg')) < 1.5 else 'Heavy'

        # Lưu lại file CSV
        df.to_csv("project_python/data/laptop_price - dataset.csv", index=False)
        messagebox.showinfo("Thành công", f"Dữ liệu của model '{model_name}' đã được cập nhật thành công!")
        window.destroy()

    # Nút cập nhật
    update_button = tk.Button(window, text="Cập nhật", command=save_changes, font=("Arial", 12, "bold"), bg="#2E7D32", fg="white")
    update_button.pack(pady=20, padx=10, fill="x")

    # Cho phép nhấn Enter để cập nhật
    update_button.bind("<Return>", lambda event: save_changes())

    window.mainloop()
