import pandas as pd

def create_laptop_record(
    company, product, typename, inches, screen_resolution,
    cpu_company, cpu_type, cpu_frequency, ram, memory,
    gpu_company, gpu_type, os, weight, price
):
    new_data = {
        'Company': company,
        'Product': product,
        'TypeName': typename,
        'Inches': inches,
        'ScreenResolution': screen_resolution,
        'CPU_Company': cpu_company,
        'CPU_Type': cpu_type,
        'CPU_Frequency (GHz)': cpu_frequency,
        'RAM (GB)': ram,
        'Memory': memory,
        'GPU_Company': gpu_company,
        'GPU_Type': gpu_type,
        'OpSys': os,
        'Weight (kg)': weight,
        'Price (Euro)': price,
    }

    try:
        # Mở tệp CSV và cập nhật dữ liệu
        file_path = "project_python/data/laptop_price - dataset.csv"
        try:
            df = pd.read_csv(file_path)
        except FileNotFoundError:
            df = pd.DataFrame(columns=new_data.keys())

        # Thêm dữ liệu mới vào DataFrame
        df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)

        # Ghi lại DataFrame vào CSV
        df.to_csv(file_path, index=False)
        return True
    except Exception as e:
        print(f"Lỗi khi ghi dữ liệu: {e}")
        return False