import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Đọc dữ liệu từ file CSV
file_path = "doanpython/data/weight_change_dataset.csv"  # Thay đổi đường dẫn nếu cần
da = pd.read_csv(file_path, sep=',')

# Hiển thị các tên cột
columns_names = da.columns
print("Column Names:", columns_names)

# Kiểm tra các giá trị thiếu
missing_values = da.isnull().sum()
print("Missing Values:\n", missing_values)

# Mô tả thống kê các cột số
print("Descriptive Statistics:\n", da.describe())

# Chọn các cột số cho ma trận tương quan
numeric_data = da.select_dtypes(include=[np.number])
corr_matrix = numeric_data.corr()

# Vẽ biểu đồ ma trận tương quan
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', square=True)
plt.title('Correlation Matrix')
plt.show()

# Vẽ biểu đồ phân phối cho các cột số
da.hist(bins=30, figsize=(14, 12), color='blue', edgecolor='black')
plt.suptitle("Histograms of Numerical Features", y=0.95)
plt.show()
