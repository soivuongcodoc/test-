import tkinter as tk
from tkinter import messagebox
import pandas as pd

def update_laptop_record(file_path, product_name):
    # Tạo cửa sổ cập nhật
    window = tk.Tk()
    window.title(f"Cập nhật thông tin: {product_name}")
    window.geometry("600x700")

    # Kiểm tra file CSV
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        messagebox.showerror("Lỗi", "Không tìm thấy tệp dữ liệu.")
        window.destroy()
        return

    # Kiểm tra sản phẩm trong dữ liệu
    if product_name not in df['Product'].values:
        messagebox.showerror("Lỗi", f"Sản phẩm '{product_name}' không tồn tại trong dữ liệu.")
        window.destroy()
        return

    # Lấy chỉ số của sản phẩm
    index = df[df['Product'] == product_name].index[0]

    # Các trường cần cập nhật
    fields = [
        'Company', 'TypeName', 'Inches', 'ScreenResolution', 'CPU_Company', 
        'CPU_Type', 'CPU_Frequency (GHz)', 'RAM (GB)', 'Memory', 
        'GPU_Company', 'GPU_Type', 'OpSys', 'Weight (kg)', 'Price (Euro)'
    ]
    entries = {}

    # Tiêu đề
    tk.Label(window, text=f"Cập nhật dữ liệu cho '{product_name}'", font=("Arial", 16, "bold")).pack(pady=10)

    # Tạo Entry cho các trường
    for field in fields:
        tk.Label(window, text=f"{field}:", font=("Arial", 10)).pack(pady=5)
        entry = tk.Entry(window, font=("Arial", 10))
        entry.insert(0, str(df.at[index, field]))
        entry.pack(fill="x", padx=10)
        entries[field] = entry

    # Hàm lưu thay đổi
    def save_changes():
        try:
            for field in fields:
                new_value = entries[field].get()
                # Kiểm tra kiểu dữ liệu
                if field in ['Inches', 'CPU_Frequency (GHz)', 'RAM (GB)', 'Weight (kg)', 'Price (Euro)']:
                    df.at[index, field] = float(new_value)
                else:
                    df.at[index, field] = new_value

            # Lưu vào file CSV
            df.to_csv(file_path, index=False)
            messagebox.showinfo("Thành công", f"Cập nhật thành công cho '{product_name}'.")
            window.destroy()
        except Exception as e:
            messagebox.showerror("Lỗi", f"Đã xảy ra lỗi khi lưu dữ liệu: {e}")

    # Nút Lưu
    tk.Button(window, text="Lưu Thay Đổi", command=save_changes, font=("Arial", 12, "bold"), bg="#2E7D32", fg="white").pack(pady=20, padx=10, fill="x")

    window.mainloop()
