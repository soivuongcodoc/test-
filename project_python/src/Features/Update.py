import tkinter as tk
from tkinter import messagebox, ttk, Canvas
import pandas as pd

def update_laptop_record(file_path, product_name):
    window = tk.Tk()
    window.title(f"Cập nhật thông tin: {product_name}")
    window.geometry("600x700")  # Giới hạn kích thước cửa sổ

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

    index = df[df['Product'] == product_name].index[0]

    fields = [
        'Company', 'TypeName', 'Inches', 'ScreenResolution', 'CPU_Company', 
        'CPU_Type', 'CPU_Frequency (GHz)', 'RAM (GB)', 'Memory', 
        'GPU_Company', 'GPU_Type', 'OpSys', 'Weight (kg)', 'Price (Euro)'
    ]
    entries = {}

    # Tạo thanh cuộn
    canvas = Canvas(window)
    scroll_y = tk.Scrollbar(window, orient="vertical", command=canvas.yview)
    frame = tk.Frame(canvas)

    # Hiển thị nội dung trong Canvas
    def on_configure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    canvas.create_window((0, 0), window=frame, anchor='nw')
    canvas.configure(yscrollcommand=scroll_y.set)

    # Tiêu đề
    tk.Label(frame, text=f"Cập nhật dữ liệu cho '{product_name}'", font=("Arial", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

    # Tạo Entry cho các trường
    for i, field in enumerate(fields):
        tk.Label(frame, text=f"{field}:", font=("Arial", 10)).grid(row=i+1, column=0, sticky='w', padx=10, pady=5)
        entry = tk.Entry(frame, font=("Arial", 10), width=30)
        entry.insert(0, str(df.at[index, field]))
        entry.grid(row=i+1, column=1, padx=10, pady=5)
        entries[field] = entry

    # Hàm lưu thay đổi
    def save_changes():
        try:
            for field in fields:
                new_value = entries[field].get()
                if field in ['Inches', 'CPU_Frequency (GHz)', 'RAM (GB)', 'Weight (kg)', 'Price (Euro)']:
                    df.at[index, field] = float(new_value)
                else:
                    df.at[index, field] = new_value

            df.to_csv(file_path, index=False)
            messagebox.showinfo("Thành công", f"Cập nhật thành công cho '{product_name}'.")
            window.destroy()
        except Exception as e:
            messagebox.showerror("Lỗi", f"Đã xảy ra lỗi khi lưu dữ liệu: {e}")

    # Nút Lưu
    tk.Button(frame, text="Lưu Thay Đổi", command=save_changes, font=("Arial", 12, "bold"), bg="#2E7D32", fg="white").grid(row=len(fields)+1, column=0, columnspan=2, pady=20, padx=10, sticky='we')

    # Hiển thị thanh cuộn
    canvas.pack(side="left", fill="both", expand=True)
    scroll_y.pack(side="right", fill="y")
    frame.bind("<Configure>", on_configure)

    window.mainloop()
