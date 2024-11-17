# 1. Installing Required Libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns

# 2. Đọc và kiểm tra dữ liệu

# Đọc dữ liệu
df = pd.read_csv('project_python/laptop_price - dataset.csv')

# Hiển thị thông tin cơ bản
print(df.info())

# Kiểm tra giá trị NaN
print("Số giá trị NaN trong dữ liệu:\n", df.isnull().sum())

# Kiểm tra giá trị trùng lặp
print("Số bản ghi trùng lặp:", df.duplicated().sum())

# 3. Nhóm dữ liệu theo công ty và vẽ biểu đồ

# Biểu đồ sản phẩm và giá cao nhất theo công ty
df.groupby("Company")[["Product", "Price (Euro)"]].max().plot(kind='bar', figsize=(10, 6), title="Giá cao nhất theo công ty")
plt.xlabel("Công ty")
plt.ylabel("Giá (Euro)")
plt.show()

# Biểu đồ kích thước trung bình theo công ty
df.groupby("Company")["Inches"].mean().plot(kind='bar', figsize=(10, 6), title="Kích thước màn hình trung bình theo công ty")
plt.xlabel("Công ty")
plt.ylabel("Kích thước màn hình (inch)")
plt.show()

# 4. Phân phối kích thước màn hình
df['Inches'].plot(kind='hist', bins=15, title="Phân phối kích thước màn hình", figsize=(10, 6))
plt.xlabel("Kích thước màn hình (inch)")
plt.ylabel("Tần suất")
plt.show()


