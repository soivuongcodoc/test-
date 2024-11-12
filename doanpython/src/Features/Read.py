import pandas as pd

def read_dataset(file_path):
    """
    Hàm đọc tệp CSV với khả năng kiểm tra phân tách là dấu phẩy hoặc dấu tab.
    
    Tham số:
    - file_path (str): Đường dẫn tới tệp CSV.
    
    Trả về:
    - pd.DataFrame: DataFrame chứa dữ liệu từ tệp CSV.
    """
    try:
        # Thử đọc file với dấu phẩy
        df = pd.read_csv(file_path, sep=',')
        print("File được đọc với dấu phẩy làm phân tách.")
    except:
        try:
            # Nếu thất bại, thử với dấu tab
            df = pd.read_csv(file_path, sep='\t')
            print("File được đọc với dấu tab làm phân tách.")
        except Exception as e:
            print(f"Lỗi khi đọc file: {e}")
            return None
    return df

if __name__ == "__main__":
    # Đường dẫn tới file
    file_path = "doanpython/data/weight_change_dataset.csv"
    
    # Đọc file
    df = read_dataset(file_path)
    
    # Hiển thị 5 dòng dữ liệu đầu tiên nếu thành công
    if df is not None:
        print("Dữ liệu đầu tiên trong file:")
        print(df.head())
    else:
        print("Không thể đọc dữ liệu từ file.")
