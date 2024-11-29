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

def convert_columns_to_numeric(df):
    """
    Hàm để chuyển đổi hai cột 'Price (Euro)' và 'Weight (kg)' sang dạng số.
    """
    # Chuyển đổi cột 'Price (Euro)'
    if 'Price (Euro)' in df.columns:
        df['Price (Euro)'] = pd.to_numeric(df['Price (Euro)'], errors='coerce')
    
    # Chuyển đổi cột 'Weight (kg)'
    if 'Weight (kg)' in df.columns:
        df['Weight (kg)'] = pd.to_numeric(df['Weight (kg)'], errors='coerce')
    
    return df


def clean_weight_column(df):
    """
    Làm sạch cột 'Weight (kg)', loại bỏ ký tự 'kg' và chuyển đổi thành số.
    """
    if 'Weight (kg)' in df.columns:
        # Đảm bảo dữ liệu là chuỗi trước khi thay thế
        df['Weight (kg)'] = df['Weight (kg)'].astype(str).str.replace('kg', '', regex=False)
        # Chuyển đổi thành số (float)
        df['Weight (kg)'] = pd.to_numeric(df['Weight (kg)'], errors='coerce')
    return df


def clean_price_column(df):
    """
    Làm sạch cột 'Price (Euro)', loại bỏ ký tự '€' và chuyển đổi thành số.
    """
    if 'Price (Euro)' in df.columns:
        # Đảm bảo dữ liệu là chuỗi trước khi thay thế
        df['Price (Euro)'] = df['Price (Euro)'].astype(str).str.replace('€', '', regex=False)
        # Chuyển đổi thành số (float)
        df['Price (Euro)'] = pd.to_numeric(df['Price (Euro)'], errors='coerce')
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
    # Bước 2: Điền giá trị thiếu cho các cột cần thiết (ví dụ: cột 'Price (Euro)')
    df = fill_missing_values(df, 'Price (Euro)', value=0)

    # Bước 3: Xóa các hàng có giá trị bị thiếu
    df = drop_missing_values(df)
    # Bước 4: Chuyển đổi các cột sang dạng số (ví dụ: 'Price' và 'Weight (kg)').
    df = convert_columns_to_numeric(df)
    df = clean_weight_column(df)
    df = clean_price_column(df)

    # Bước 5: Thay thế giá trị không hợp lệ (ví dụ: giá trị âm trong cột 'Price (Euro)')
    df = replace_invalid_values(df, 'Price (Euro)')
    df = replace_invalid_values(df, 'Weight (kg)')
    
    # Bước 6: Xóa các hàng trùng lặp
    df = remove_duplicates(df)

    # Bước 7: Lưu dữ liệu đã làm sạch vào cùng đường dẫn với file gốc
    save_cleaned_data(df, file_path)

