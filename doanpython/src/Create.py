import pandas as pd

def create_record(file_path, new_data):
    # Hàm thêm một bản ghi mới vào dataset.
    try:
        # Đọc dữ liệu hiện tại
        df = pd.read_csv(file_path)
        
        # Chuyển dữ liệu mới vào DataFrame và thêm vào dataset hiện có
        new_record = pd.DataFrame([new_data])
        df = pd.concat([df, new_record], ignore_index=True)
        
        # Ghi lại dữ liệu vào file
        df.to_csv(file_path, index=False)
        print("Bản ghi mới đã được thêm thành công.")
        
        return df  # Trả về dataset đã cập nhật
    except Exception as e:
        print(f"Lỗi khi thêm bản ghi: {e}")
        return None

