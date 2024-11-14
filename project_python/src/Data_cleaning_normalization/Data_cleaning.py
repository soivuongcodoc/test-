import pandas as pd
import numpy as np

file_path = "project_python/data/laptop_price - dataset.csv"

def load_data(file_path):
    """
    Hàm để đọc dữ liệu từ tệp CSV.
    """
    return pd.read_csv(file_path)

def drop_missing_values(df):
    """
    Hàm để xóa các hàng có giá trị bị thiếu.
    """
    df_cleaned = df.dropna()
    return df_cleaned

def fill_missing_values(df, column, value=np.nan):
    """
    Hàm để điền giá trị mặc định vào các giá trị thiếu trong cột.
    
    Parameters:
    - df (DataFrame): Dữ liệu cần xử lý.
    - column (str): Cột cần điền giá trị thiếu.
    - value (default=np.nan): Giá trị điền vào (mặc định là NaN).
    """
    df[column] = df[column].fillna(value)
    return df

def convert_columns_to_numeric(df, columns):
    """
    Hàm để chuyển đổi các cột sang dạng số.
    
    Parameters:
    - df (DataFrame): Dữ liệu cần xử lý.
    - columns (list): Danh sách các cột cần chuyển đổi.
    """
    for column in columns:
        df[column] = pd.to_numeric(df[column], errors='coerce')
    return df

def clean_weight_column(df):
    """
    Hàm để làm sạch cột trọng lượng, loại bỏ các ký tự không cần thiết.
    Giả sử cột trọng lượng có tên là 'Weight (kg)' và chứa các ký tự như 'kg'.
    """
    df['Weight (kg)'] = df['Weight (kg)'].str.replace('kg', '').astype(float)
    return df

def clean_price_column(df):
    """
    Hàm để làm sạch cột 'Price (Euro)', loại bỏ ký tự '€' và chuyển đổi thành số.
    Giả sử cột giá có tên là 'Price (Euro)' và chứa ký tự '€'.
    """
    df['Price (Euro)'] = df['Price (Euro)'].str.replace('€', '').astype(float)
    return df

def remove_duplicates(df):
    """
    Hàm để xóa các hàng trùng lặp.
    """
    df_cleaned = df.drop_duplicates()
    return df_cleaned

def replace_invalid_values(df, column, invalid_value=np.nan):
    """
    Hàm để thay thế các giá trị không hợp lệ trong cột với giá trị mặc định.
    
    """
    df[column] = np.where(df[column] < 0, invalid_value, df[column])
    return df

def save_cleaned_data(df, file_path):
    """
    Hàm để lưu dữ liệu đã làm sạch vào tệp CSV 
    """
    df.to_csv(file_path, index=False)

def clean_data(file_path):
    """
    Hàm chính để làm sạch dữ liệu và lưu kết quả vào tệp đã cho.
    """
    # Bước 1: Tải dữ liệu
    df = load_data(file_path)

    # Bước 2: Xóa các hàng có giá trị bị thiếu
    df = drop_missing_values(df)

    # Bước 3: Điền giá trị thiếu cho các cột cần thiết (ví dụ: cột 'Price (Euro)')
    df = fill_missing_values(df, 'Price (Euro)', value=0)

    # Bước 4: Chuyển đổi các cột sang dạng số (ví dụ: 'Price' và 'Weight (kg)').
    df = convert_columns_to_numeric(df, ['Price'])
    df = clean_weight_column(df)
    df = clean_price_column(df)

    # Bước 5: Thay thế giá trị không hợp lệ (ví dụ: giá trị âm trong cột 'Price (Euro)')
    df = replace_invalid_values(df, 'Price (Euro)')

    # Bước 6: Xóa các hàng trùng lặp
    df = remove_duplicates(df)

    # Bước 7: Lưu dữ liệu đã làm sạch vào cùng đường dẫn với file gốc
    save_cleaned_data(df, file_path)

