import pandas as pd

def load_data(file_path):
    file_path= "project_python/data/laptop_price - dataset.csv"
    """Hàm để đọc dữ liệu từ tệp CSV."""
    return pd.read_csv(file_path)

def normalize_text_columns(df):
    """Chuẩn hóa các cột văn bản bằng cách loại bỏ khoảng trắng và chuyển đổi sang chữ thường."""
    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].str.strip().str.lower()
    return df

# def standardize_column_names(df):
#     """Chuẩn hóa tên cột bằng cách chuyển đổi sang chữ thường và thay thế dấu cách bằng dấu gạch dưới."""
#     df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]
#     return df

def convert_data_types(df):
    """Chuyển đổi các cột cụ thể thành các kiểu dữ liệu thích hợp"""
    if 'ram_(gb)' in df.columns:
        df['ram_(gb)'] = df['ram_(gb)'].astype(int)
    if 'price_(euro)' in df.columns:
        df['price_(euro)'] = df['price_(euro)'].astype(float)
    return df

def normalize_dataset(file_path):
    """ Chạy tất cả các bước chuẩn hóa trên tập dữ liệu và trả về DataFrame đã chuẩn hóa."""
    df = load_data(file_path)
    df = normalize_text_columns(df)
    # df = standardize_column_names(df)
    df = convert_data_types(df)
    return df


