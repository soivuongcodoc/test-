import tkinter as tk
from tkinter import messagebox, ttk
import pandas as pd
import sys
sys.path.append("project_python/src")
from Features import Search
from Features import Sort
from Features import Create  
from Features import Update
from Features.Delete import delete_laptop_record
from Features.Chart import load_and_check_data, plot_price_by_company, plot_avg_screen_size_by_company, plot_screen_size_distribution
from Data_cleaning_normalization.Data_cleaning import clean_data
from Data_cleaning_normalization.Data_normalizer import normalize_dataset

def run_interface():
    # Các biến toàn cục cho phân trang
    current_page = 1
    items_per_page = 300
    total_pages = 1
    df_data = None

    # Hàm hiển thị dữ liệu theo trang
    def display_page():
        nonlocal current_page, total_pages, df_data
        tree.delete(*tree.get_children())  # Xóa dữ liệu cũ trên Treeview

        # Lấy dữ liệu của trang hiện tại
        start_idx = (current_page - 1) * items_per_page
        end_idx = start_idx + items_per_page

        for row in df_data.iloc[start_idx:end_idx].itertuples(index=False):
            tree.insert("", "end", values=list(row))

        # Cập nhật nhãn hiển thị số trang
        label_pagination.config(text=f"Trang {current_page}/{total_pages}")
        update_pagination_buttons()

    # Hàm đọc dữ liệu và thiết lập phân trang
    def read_data():
        nonlocal current_page, total_pages, df_data
        try:
            # Đọc dữ liệu từ tệp CSV
            df_data = pd.read_csv("project_python/data/laptop_price - dataset.csv")

            # Tính tổng số trang
            total_pages = (len(df_data) + items_per_page - 1) // items_per_page
            current_page = 1
            for col in columns:
                 tree.heading(col, text=col)
                 if col == "ScreenResolution":
                    tree.column(col, width=300, anchor='center', stretch=False)  # Đặt chiều rộng lớn hơn cho cột 'ScreenResolution'
                 else:
                    tree.column(col, width=150, anchor='center', stretch=False)  # Các cột khác giữ nguyên


            # Hiển thị trang đầu tiên
            display_page()
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể đọc dữ liệu: {e}")

    # Hàm chuyển sang trang trước
    def go_to_previous_page():
        nonlocal current_page
        if current_page > 1:
            current_page -= 1
            display_page()

    # Hàm chuyển sang trang sau
    def go_to_next_page():
        nonlocal current_page, total_pages
        if current_page < total_pages:
            current_page += 1
            display_page()

    # Hàm cập nhật trạng thái nút phân trang
    def update_pagination_buttons():
        btn_prev["state"] = "normal" if current_page > 1 else "disabled"
        btn_next["state"] = "normal" if current_page < total_pages else "disabled"

    def display_search_result():
        company_name = entry_search.get()
        if not company_name:
            messagebox.showwarning("Cảnh báo", "Vui lòng nhập Company để tìm kiếm.")
            return

        try:
            # Gọi hàm tìm kiếm
            result = Search.search_by_company(company_name)

            # Xóa các dòng hiện tại trong TreeView
            for row in tree.get_children():
                tree.delete(row)

            # Hiển thị kết quả
            if not result.empty:
                for _, row in result.iterrows():
                    tree.insert("", "end", values=list(row))
            else:
                messagebox.showinfo("Thông báo", f"Không tìm thấy kết quả cho Company '{company_name}'")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Đã xảy ra lỗi khi tìm kiếm: {e}")

    # Hàm hiển thị dữ liệu sau khi sắp xếp
    def display_sorted_data(sort_func, ascending):
        try:
            df_sorted = sort_func("project_python/data/laptop_price - dataset.csv", ascending)

            for row in tree.get_children():
                tree.delete(row)

            for _, row in df_sorted.iterrows():
                tree.insert("", "end", values=list(row))

            messagebox.showinfo("Thành công", "Dữ liệu đã được sắp xếp.")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể sắp xếp dữ liệu: {e}")

    # Hàm mở cửa sổ thêm bản ghi mới
    def open_create_window():
        def add_record():
            try:
                # Lấy dữ liệu từ các Entry
                new_data = {
                    "company": entry_company.get(),
                    "product": entry_product.get(),
                    "typename": entry_typename.get(),
                    "inches": float(entry_inches.get()),
                    "screen_resolution": entry_screen_resolution.get(),
                    "cpu_company": entry_cpu_company.get(),
                    "cpu_type": entry_cpu_type.get(),
                    "cpu_frequency": float(entry_cpu_frequency.get()),
                    "ram": int(entry_ram.get()),
                    "memory": entry_memory.get(),
                    "gpu_company": entry_gpu_company.get(),
                    "gpu_type": entry_gpu_type.get(),
                    "os": entry_os.get(),
                    "weight": float(entry_weight.get()),
                    "price": float(entry_price.get())
                }

                # Gọi hàm trong module Create
                success = Create.create_laptop_record(**new_data)
                if success:
                    messagebox.showinfo("Thành công", "Bản ghi mới đã được thêm.")
                    # Tải lại dữ liệu lên giao diện
                    read_data()
                    create_window.destroy()
                else:
                    messagebox.showerror("Lỗi", "Không thể thêm bản ghi vào dataset.")
            except ValueError as ve:
                messagebox.showerror("Lỗi", f"Dữ liệu nhập vào không hợp lệ: {ve}")
            except Exception as e:
                messagebox.showerror("Lỗi", f"Đã xảy ra lỗi: {e}")

        # Tạo cửa sổ để thêm dữ liệu mới
        create_window = tk.Toplevel(root)
        create_window.title("Thêm Laptop Mới")
        create_window.geometry("600x500")

        labels = [
            "Company", "Product", "TypeName", "Inches", "Screen Resolution",
            "CPU Company", "CPU Type", "CPU Frequency", "RAM", "Memory",
            "GPU Company", "GPU Type", "OS", "Weight", "Price"
        ]

        entries = {}
        for i, label in enumerate(labels):
            ttk.Label(create_window, text=label, font=("Arial", 10)).grid(row=i // 4, column=(i % 4) * 2, padx=5, pady=5, sticky="e")
            entry = ttk.Entry(create_window, width=20)
            entry.grid(row=i // 4, column=(i % 4) * 2 + 1, padx=5, pady=5)
            entries[label.lower().replace(" ", "_")] = entry

        entry_company = entries["company"]
        entry_product = entries["product"]
        entry_typename = entries["typename"]
        entry_inches = entries["inches"]
        entry_screen_resolution = entries["screen_resolution"]
        entry_cpu_company = entries["cpu_company"]
        entry_cpu_type = entries["cpu_type"]
        entry_cpu_frequency = entries["cpu_frequency"]
        entry_ram = entries["ram"]
        entry_memory = entries["memory"]
        entry_gpu_company = entries["gpu_company"]
        entry_gpu_type = entries["gpu_type"]
        entry_os = entries["os"]
        entry_weight = entries["weight"]
        entry_price = entries["price"]

        button_add_record = ttk.Button(create_window, text="Thêm Bản Ghi", command=add_record)
        button_add_record.grid(row=len(labels) // 4 + 1, column=1, pady=10)
    
    # Tạo cửa sổ để vẽ biểu đồ
    def open_chart_window():
        file_path = "project_python/data/laptop_price - dataset.csv"
        df = load_and_check_data(file_path)

        if df is not None:
            # Tạo cửa sổ mới
            chart_window = tk.Toplevel(root)
            chart_window.title("Biểu Đồ Dữ Liệu Laptop")
            chart_window.geometry("400x300")

            tk.Label(chart_window, text="Chọn biểu đồ để hiển thị:", font=("Arial", 14, "bold")).pack(pady=10)

            # Nút biểu đồ giá cao nhất theo công ty
            ttk.Button(
                chart_window, text="Giá cao nhất theo công ty", command=lambda: plot_price_by_company(df)
            ).pack(pady=5)

            # Nút biểu đồ kích thước trung bình theo công ty
            ttk.Button(
                chart_window, text="Kích thước màn hình trung bình", command=lambda: plot_avg_screen_size_by_company(df)
            ).pack(pady=5)

            # Nút biểu đồ phân phối kích thước màn hình
            ttk.Button(
                chart_window, text="Phân phối kích thước màn hình", command=lambda: plot_screen_size_distribution(df)
            ).pack(pady=5)

    # Hàm xử lý xóa laptop theo tên Product
    def delete_record_by_product():
        product_name = entry_delete_product.get().strip()  # Lấy tên sản phẩm từ Entry
        if not product_name:
            messagebox.showwarning("Cảnh báo", "Vui lòng nhập tên sản phẩm để xóa.")
            return

        # Hiển thị hộp thoại xác nhận xóa
        confirm = messagebox.askyesno("Xác nhận xóa", f"Bạn có chắc chắn muốn xóa laptop có tên sản phẩm '{product_name}' không?")
        
        if confirm:
            # Nếu người dùng xác nhận, gọi hàm xóa laptop
            success = delete_laptop_record(product_name)
            if success:
                # Cập nhật lại TreeView sau khi xóa
                read_data()
        else:
            messagebox.showinfo("Thông báo", "Không có gì thay đổi. Bản ghi không bị xóa.")
    # Hàm mở giao diện cập nhật
    def open_update_window():
        selected_item = tree.focus()  # Lấy item được chọn trong Treeview
        if not selected_item:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn một sản phẩm để cập nhật.")
            return

        # Lấy tên sản phẩm từ Treeview
        product_name = tree.item(selected_item, "values")[1]  # Cột 'Product' ở vị trí thứ 1
        file_path = "project_python/data/laptop_price - dataset.csv"

        # Gọi giao diện cập nhật
        Update.update_laptop_record(file_path, product_name)

        # Tải lại dữ liệu sau khi cập nhật
        read_data()
    def clean():
        file_path = "project_python/data/laptop_price - dataset.csv"
        clean_data(file_path)
    def normal():
        file_path ="project_python/data/laptop_price - dataset.csv"
        normalize_dataset(file_path)

    # Thiết lập giao diện tkinter
    root = tk.Tk()
    root.title("Dữ liệu Giá Laptop")
    root.geometry("1200x900")
    root.configure(bg="#f7f7f7")

    # Frame chính
    main_frame = ttk.Frame(root, padding="15")
    main_frame.pack(fill="both", expand=True)

    # Tiêu đề
    label_title = ttk.Label(main_frame, text="Dữ liệu Giá Laptop", font=("Arial", 20, "bold"), foreground="#333333")
    label_title.pack(pady=(10, 20))

    # Cột dữ liệu
    columns = [
        "Company", "Product", "TypeName", "Inches", "ScreenResolution",
        "CPU_Company", "CPU_Type", "CPU_Frequency (GHz)", "RAM (GB)", "Memory",
        "GPU_Company", "GPU_Type", "OpSys", "Weight (kg)", "Price (Euro)"
    ]

    # Treeview hiển thị dữ liệu
    tree_frame = ttk.Frame(main_frame)
    tree_frame.pack(fill="both", expand=True)

    # Tạo Treeview
    tree = ttk.Treeview(tree_frame, columns=columns, show="headings", height=20)

    # Định nghĩa cột
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=150, anchor='center', stretch=False)

    # Thêm thanh cuộn dọc
    scrollbar_y = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar_y.set)
    scrollbar_y.pack(side="right", fill="y")

    # Thêm thanh cuộn ngang
    scrollbar_x = ttk.Scrollbar(tree_frame, orient="horizontal", command=tree.xview)
    tree.configure(xscrollcommand=scrollbar_x.set)
    scrollbar_x.pack(side="bottom", fill="x")

    # Hiển thị Treeview
    tree.pack(side="left", fill="both", expand=True)

    # Đảm bảo kích thước khung Treeview luôn được điều chỉnh theo kích thước giao diện
    tree_frame.pack_propagate(False)
     # Khung chứa nút và thông tin phân trang
    frame_pagination = ttk.Frame(root)
    frame_pagination.pack(pady=10)

    # Nhãn hiển thị số trang
    label_pagination = ttk.Label(frame_pagination, text=f"Trang {current_page}/{total_pages}", font=("Arial", 12))
    label_pagination.pack(side="left", padx=10)

    # Nút chuyển trang trước
    btn_prev = ttk.Button(frame_pagination, text="Trang trước", command=go_to_previous_page)
    btn_prev.pack(side="left", padx=5)

    # Nút chuyển trang sau
    btn_next = ttk.Button(frame_pagination, text="Trang sau", command=go_to_next_page)
    btn_next.pack(side="left", padx=5)

    # Khu vực tìm kiếm
    search_frame = ttk.Frame(main_frame)
    search_frame.pack(pady=10)

    label_search = ttk.Label(search_frame, text="Nhập Company:", font=("Arial", 12))
    label_search.pack(side="left", padx=(0, 10))

    entry_search = ttk.Entry(search_frame, width=30)
    entry_search.pack(side="left", padx=(0, 10))

    button_search = ttk.Button(search_frame, text="Tìm kiếm", command=display_search_result)
    button_search.pack(side="left")

    # Nút tải dữ liệu
    button_load_data = ttk.Button(main_frame, text="Tải Dữ liệu", command=read_data, width=25)
    button_load_data.pack(pady=10)

    # Nút tạo laptop mới
    button_create = ttk.Button(main_frame, text="Tạo Laptop Mới", command=open_create_window, width=25)
    button_create.pack(pady=10)
    # Nút làm sạch và chuẩn hóa dữ liệu
    data_cleaning_frame = ttk.Frame(main_frame)
    data_cleaning_frame.pack(pady=10)

    button_clean_data = ttk.Button(data_cleaning_frame, text="Làm sạch dữ liệu", command=clean, width=25)
    button_clean_data.pack(side="left", padx=(0, 10))

    button_normalize_data = ttk.Button(data_cleaning_frame, text="Chuẩn hóa dữ liệu", command=normal, width=25)
    button_normalize_data.pack(side="left", padx=(0, 10))

    # Khu vực xóa laptop
    delete_frame = ttk.Frame(main_frame)
    delete_frame.pack(pady=10)

    # Label và Entry để nhập tên sản phẩm cần xóa
    label_delete_product = ttk.Label(delete_frame, text="Nhập tên sản phẩm để xóa:", font=("Arial", 12))
    label_delete_product.pack(side="left", padx=(0, 10))

    entry_delete_product = ttk.Entry(delete_frame, width=30)
    entry_delete_product.pack(side="left", padx=(0, 10))

    # Nút xóa
    button_delete = ttk.Button(delete_frame, text="Xóa Laptop", command=delete_record_by_product, width=25)
    button_delete.pack(side="left", padx=(0, 10))

    # Nút cập nhật
    button_update = ttk.Button(main_frame, text="Cập nhật Laptop", command=open_update_window, width=25)
    button_update.pack(pady=10)

    # Thêm nút "Vẽ Biểu Đồ" vào giao diện chính
    button_chart = ttk.Button(main_frame, text="Vẽ Biểu Đồ", command=open_chart_window, width=25)
    button_chart.pack(pady=10)

    # Khu vực sắp xếp
    sort_frame = ttk.Frame(main_frame)
    sort_frame.pack(pady=10)

    ttk.Label(sort_frame, text="Sắp xếp theo:", font=("Arial", 12)).pack(side="left", padx=(0, 10))

    button_sort_name = ttk.Button(sort_frame, text="Tên công ty (A-Z)", 
                                  command=lambda: display_sorted_data(Sort.sort_laptops_by_name, True))
    button_sort_name.pack(side="left", padx=(0, 10))

    button_sort_price = ttk.Button(sort_frame, text="Giá (thấp đến cao)", 
                                   command=lambda: display_sorted_data(Sort.sort_laptops_by_price, True))
    button_sort_price.pack(side="left", padx=(0, 10))

    button_sort_weight = ttk.Button(sort_frame, text="Trọng lượng (nhẹ đến nặng)", 
                                    command=lambda: display_sorted_data(Sort.sort_laptops_by_weight, True))
    button_sort_weight.pack(side="left", padx=(0, 10))

    root.mainloop()
