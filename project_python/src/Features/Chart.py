import pandas as pd
import matplotlib.pyplot as plt

def load_and_check_data(file_path):
    """
    Đọc dữ liệu, kiểm tra thông tin, giá trị NaN và trùng lặp.
    """
    try:
        df = pd.read_csv(file_path)
        print("Thông tin dữ liệu:")
        print(df.info())
        print("\nSố giá trị NaN trong dữ liệu:")
        print(df.isnull().sum())
        print("\nSố bản ghi trùng lặp:", df.duplicated().sum())
        return df
    except FileNotFoundError:
        print("Không tìm thấy file dữ liệu.")
        return None

def plot_price_by_company(df):
    """
    Biểu đồ giá cao nhất theo công ty.
    """
    df.groupby("Company")[["Product", "Price (Euro)"]].max().plot(
        kind='bar', figsize=(10, 6), title="Giá cao nhất theo công ty"
    )
    plt.xlabel("Công ty")
    plt.ylabel("Giá (Euro)")
    plt.show()

def plot_avg_screen_size_by_company(df):
    """
    Biểu đồ kích thước trung bình theo công ty.
    """
    df.groupby("Company")["Inches"].mean().plot(
        kind='bar', figsize=(10, 6), title="Kích thước màn hình trung bình theo công ty"
    )
    plt.xlabel("Công ty")
    plt.ylabel("Kích thước màn hình (inch)")
    plt.show()

def plot_screen_size_distribution(df):
    """
    Biểu đồ phân phối kích thước màn hình.
    """
    df['Inches'].plot(kind='hist', bins=15, title="Phân phối kích thước màn hình", figsize=(10, 6))
    plt.xlabel("Kích thước màn hình (inch)")
    plt.ylabel("Tần suất")
    plt.show()
