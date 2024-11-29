# Search.py
import pandas as pd

def search_by_company(company_name):
    try:
        file_path = "project_python/data/laptop_price - dataset.csv"
        df = pd.read_csv(file_path)
        return df[df['Company'].str.contains(company_name, case=False, na=False)]
    except Exception as e:
        print(f"Lỗi khi tìm kiếm: {e}")
        return pd.DataFrame()
