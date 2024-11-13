import tkinter as tk
from tkinter import messagebox
import pandas as pd
import Read

def delete_laptop_record(model_name):

    # Xóa bản ghi laptop dựa trên tên model.

    try:
        # Đọc dữ liệu từ file CSV
        df = pd.read_csv("project_python/laptop_price - dataset.csv")

        # Kiểm tra xem model có tồn tại trong dữ liệu không
        if model_name in df['Model'].values:
            # Xóa bản ghi tương ứng
            df = df[df['Model'] != model_name]

            # Lưu lại file CSV
            df.to_csv("project_python/laptop_price - dataset.csv", index=False)

            messagebox.showinfo("Thành công", f"Bản ghi của model '{model_name}' đã được xóa thành công!")
        else:
            messagebox.showerror("Lỗi", f"Model '{model_name}' không tồn tại trong dữ liệu.")

        return df

    except FileNotFoundError:
        messagebox.showerror("Lỗi", "Không tìm thấy file CSV.")
        return None