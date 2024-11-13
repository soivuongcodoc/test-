import pandas as pd
import Read

def create_laptop_record(brand, model, processor, ram, storage, screen_size, price, os, weight):

    # Tạo một từ điển chứa dữ liệu mới
    new_data = {
        'Brand': brand,
        'Model': model,
        'Processor': processor,
        'RAM': ram,
        'Storage': storage,
        'Screen Size': screen_size,
        'Price': price,
        'Operating System': os,
        'Weight': weight
    }

    # Tính toán các thông tin bổ sung nếu cần thiết
    new_data['Price in Thousands'] = round(price / 1000, 2) if price > 0 else 0
    new_data['Weight Category'] = 'Light' if float(weight.strip('kg')) < 1.5 else 'Heavy'

    # Đọc dữ liệu hiện có từ file CSV
    try:
        df = pd.read_csv("project_python/laptop_price - dataset.csv")
    except FileNotFoundError:
        # Nếu file không tồn tại, tạo một DataFrame mới với cấu trúc cột phù hợp
        df = pd.DataFrame(columns=['Brand', 'Model', 'Processor', 'RAM', 'Storage', 'Screen Size', 'Price', 'Operating System', 'Weight', 'Price in Thousands', 'Weight Category'])

    # Thêm dữ liệu mới vào DataFrame
    new_record_df = pd.DataFrame([new_data])
    df = pd.concat([df, new_record_df], ignore_index=True)

    # Lưu lại DataFrame vào file CSV
    df.to_csv("project_python/laptop_price - dataset.csv", index=False)

    return df