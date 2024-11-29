import pandas as pd

def sort_laptops_by_name(df, ascending=True):
    """
    Hàm sắp xếp danh sách laptop theo tên công ty.
    """
    df = pd.read_csv("project_python/data/laptop_price - dataset.csv")
    df_sorted = df.sort_values(by="Company", ascending=ascending)
    return df_sorted

def sort_laptops_by_price(df, ascending=True):
    """
    Hàm sắp xếp danh sách laptop theo giá.
    """
    df = pd.read_csv("project_python/data/laptop_price - dataset.csv")
    df_sorted = df.sort_values(by="Price (Euro)", ascending=ascending)
    return df_sorted

def sort_laptops_by_weight(df, ascending=True):
    """
    Hàm sắp xếp danh sách laptop theo trọng lượng.
    """
    df = pd.read_csv("project_python/data/laptop_price - dataset.csv")
    df_sorted = df.sort_values(by="Weight (kg)", ascending=ascending)
    return df_sorted
