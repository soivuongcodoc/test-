import tkinter as tk
from tkinter import messagebox
import pandas as pd

def delete_record_by_attribute(attribute, value):
    try:
        # Đọc dữ liệu từ file CSV
        df = pd.read_csv("project_python/laptop_price - dataset.csv")

        # Kiểm tra xem thuộc tính có tồn tại không
        if attribute not in df.columns:
            messagebox.showerror("Lỗi", f"Thuộc tính '{attribute}' không tồn tại trong dữ liệu.")
            return None

        # Kiểm tra xem giá trị có tồn tại trong thuộc tính không
        if value in df[attribute].values:
            # Xóa các bản ghi có giá trị tương ứng
            df = df[df[attribute] != value]

            # Lưu lại file CSV
            df.to_csv("project_python/laptop_price - dataset.csv", index=False)

            messagebox.showinfo("Thành công", f"Bản ghi với '{attribute}' = '{value}' đã được xóa thành công!")
        else:
            messagebox.showerror("Lỗi", f"Không tìm thấy bản ghi với '{attribute}' = '{value}'.")

        return df

    except FileNotFoundError:
        messagebox.showerror("Lỗi", "Không tìm thấy file CSV.")
        return None
