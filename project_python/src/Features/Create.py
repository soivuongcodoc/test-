import pandas as pd
import Read

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
        'Price (Euro)': price
    }

    # Price_per_Inch: Giá mỗi inch màn hình.
    # Performance_Index: Chỉ số hiệu suất dựa trên tần số CPU, RAM và trọng lượng.
    new_data['Price_per_GB_RAM'] = round(price / ram, 2) if ram > 0 else 0
    new_data['Price_per_Inch'] = round(price / inches, 2) if inches > 0 else 0
    new_data['Performance_Index'] = round((cpu_frequency * ram) / weight, 2) if weight > 0 else 0

    # Read the existing dataset
    try:
        df = pd.read_csv("project_python/laptop_price - dataset.csv")
    except FileNotFoundError:
        # If file does not exist, create an empty DataFrame with the appropriate columns
        df = pd.DataFrame(columns=new_data.keys())

    # Append the new record
    new_record_df = pd.DataFrame([new_data])
    df = pd.concat([df, new_record_df], ignore_index=True)

    # Save the updated dataset back to CSV
    df.to_csv("project_python/laptop_price - dataset.csv", index=False)

    return df