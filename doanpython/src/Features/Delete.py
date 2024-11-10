import pandas as pd

def delete_record(file_path, participant_id):
    """
    Xóa một bản ghi trong dataset dựa trên Participant ID.
    
    Parameters:
        file_path (str): Đường dẫn tới file CSV.
        participant_id (int): ID của người tham gia cần xóa.
        
    Returns:
        DataFrame hoặc None: Dataset sau khi xóa bản ghi nếu thành công,
                             hoặc None nếu có lỗi xảy ra.
    """
    try:
        # Đọc dữ liệu hiện tại từ file
        df = pd.read_csv(file_path)
        
        # Kiểm tra nếu Participant ID tồn tại trong dataset
        if participant_id in df['Participant ID'].values:
            # Xóa bản ghi tương ứng với Participant ID
            df = df[df['Participant ID'] != participant_id]
            
            # Lưu lại dataset đã cập nhật vào file CSV
            df.to_csv(file_path, index=False)
            print(f"Bản ghi với Participant ID {participant_id} đã được xóa.")
        else:
            print(f"Participant ID {participant_id} không tồn tại trong dataset.")
        
        return df  # Trả về dataset đã cập nhật
    except Exception as e:
        print(f"Lỗi khi xóa bản ghi: {e}")
        return None
