from tkinter import messagebox
import pandas as pd
from Features import Read

def delete(participant_id_to_delete):
    try:
        # Đọc dữ liệu hiện tại
        df = Read.read()

        # Kiểm tra xem ID có tồn tại trong DataFrame hay không
        if participant_id_to_delete in df['Participant ID'].values:
            # Xóa bản ghi tương ứng
            df = df[df['Participant ID'] != participant_id_to_delete]
            df.to_csv("doanpython/data/weight_change_dataset.csv", index=False)

            messagebox.showinfo("Thành công", f"Bản ghi của ID '{participant_id_to_delete}' đã được xóa thành công!")
        else:
            messagebox.showerror("Lỗi", f"ID '{participant_id_to_delete}' không tồn tại trong DataFrame.")

        return df

    except FileNotFoundError:
        messagebox.showerror("Lỗi", "Không tìm thấy file CSV.")
        return None
