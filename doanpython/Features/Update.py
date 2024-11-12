import tkinter as tk
from tkinter import messagebox, ttk
from Features import Read

def update_record(participant_id):
    # Tạo cửa sổ cập nhật dữ liệu
    window = tk.Tk()
    window.title("Cập nhật dữ liệu người tham gia")
    window.geometry("600x700")
    window.config(bg="#E8F5E9")

    try:
        df = Read.read()
    except FileNotFoundError:
        messagebox.showerror("Lỗi", "Không tìm thấy file CSV.")
        window.destroy()
        return

    # Kiểm tra xem ID có tồn tại trong dữ liệu không
    if participant_id not in df['Participant ID'].values:
        messagebox.showerror("Lỗi", f"ID '{participant_id}' không tồn tại trong dữ liệu.")
        window.destroy()
        return

    index = df[df['Participant ID'] == participant_id].index[0]

    # Thông tin cần cập nhật
    fields = ['Age', 'Gender', 'Current Weight (lbs)', 'BMR (Calories)', 
              'Daily Calories Consumed', 'Daily Caloric Surplus/Deficit', 
              'Weight Change (lbs)', 'Duration (weeks)', 'Physical Activity Level', 
              'Sleep Quality', 'Stress Level', 'Final Weight (lbs)']
    entries = {}

    # Tiêu đề
    tk.Label(window, text=f"Cập nhật dữ liệu cho ID '{participant_id}'", font=("Arial", 16, "bold"), bg="#E8F5E9").pack(pady=10)

    # Tạo các ô nhập liệu cho từng trường thông tin
    for idx, field in enumerate(fields):
        tk.Label(window, text=f"{field}:", font=("Arial", 10), bg="#E8F5E9").pack(pady=5)
        
        entry = tk.Entry(window, font=("Arial", 10))
        entry.pack(fill="x", padx=10)
        entries[field] = entry

        # Ràng buộc phím Enter, Up, và Down để chuyển đến ô tiếp theo hoặc lưu thay đổi
        entry.bind("<Return>", lambda event, idx=idx: focus_next(idx))
        entry.bind("<Down>", lambda event, idx=idx: focus_next(idx))
        entry.bind("<Up>", lambda event, idx=idx: focus_previous(idx))

    # Hàm chuyển đến ô nhập liệu tiếp theo
    def focus_next(idx):
        if idx + 1 < len(fields):
            next_widget = entries[fields[idx + 1]]
            next_widget.focus_set()
        else:
            save_changes()  # Thực hiện cập nhật khi nhấn Enter ở ô cuối cùng

    # Hàm chuyển đến ô nhập liệu trước đó
    def focus_previous(idx):
        if idx > 0:
            previous_widget = entries[fields[idx - 1]]
            previous_widget.focus_set()

    # Hàm xử lý khi nhấn nút "Cập nhật"
    def save_changes():
        for field in fields:
            new_value = entries[field].get()
            if new_value:
                df.at[index, field] = new_value

        # Lưu dữ liệu đã cập nhật vào CSV
        df.to_csv("doanpython/data/weight_change_dataset.csv", index=False)
        messagebox.showinfo("Thành công", f"Dữ liệu của ID '{participant_id}' đã được cập nhật thành công!")
        window.destroy()

    # Nút cập nhật
    update_button = tk.Button(window, text="Cập nhật", command=save_changes, font=("Arial", 12, "bold"), bg="#2E7D32", fg="white")
    update_button.pack(pady=20, padx=10, fill="x")
    
    # Cho phép nhấn Enter tại nút cập nhật để thực hiện cập nhật
    update_button.bind("<Return>", lambda event: save_changes())

    window.mainloop()
