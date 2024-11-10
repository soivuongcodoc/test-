import pandas as pd

# Thử đọc file với phân tách là dấu phẩy
try:
    df = pd.read_csv("weight_change_dataset.csv", sep = '\t')
    print("File được đọc với dấu phẩy làm phân tách.")
except:
    try:
        # Nếu thất bại, thử với dấu tab
        df = pd.read_csv("weight_change_dataset.csv", sep="\t")
        print("File được đọc với dấu tab làm phân tách.")
    except Exception as e:
        print(f"Lỗi khi đọc file: {e}")
