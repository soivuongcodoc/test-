import pandas as pd
from tkinter import messagebox

def delete_laptop_record(product_name):
    try:
        # Đọc dữ liệu từ file CSV
        df = pd.read_csv("project_python/data/laptop_price - dataset.csv")

        # Kiểm tra xem sản phẩm có tồn tại trong dữ liệu không
        if product_name in df['Product'].values:
            # Xóa bản ghi tương ứng
            df = df[df['Product'] != product_name]

            # Lưu lại file CSV
            df.to_csv("project_python/data/laptop_price - dataset.csv", index=False)

            messagebox.showinfo("Thành công", f"Bản ghi của sản phẩm '{product_name}' đã được xóa thành công!")
        else:
            messagebox.showerror("Lỗi", f"Sản phẩm '{product_name}' không tồn tại trong dữ liệu.")

        return True

    except FileNotFoundError:
        messagebox.showerror("Lỗi", "Không tìm thấy file CSV.")
        return None
