import pandas as pd
from Features import Read

def add_weight_change_record(participant_id, age, gender, current_weight, bmr, daily_calories, 
                             caloric_surplus_deficit, weight_change, duration, activity_level, 
                             sleep_quality, stress_level, final_weight):

    new_data = {
        'Participant ID': participant_id,
        'Age': age,
        'Gender': gender,
        'Current Weight (lbs)': current_weight,
        'BMR (Calories)': bmr,
        'Daily Calories Consumed': daily_calories,
        'Daily Caloric Surplus/Deficit': caloric_surplus_deficit,
        'Weight Change (lbs)': weight_change,
        'Duration (weeks)': duration,
        'Physical Activity Level': activity_level,
        'Sleep Quality': sleep_quality,
        'Stress Level': stress_level,
        'Final Weight (lbs)': final_weight
    }
    
    # Đọc dữ liệu hiện tại
    df = Read.read()

    # Thêm bản ghi mới vào DataFrame
    new_record_df = pd.DataFrame([new_data])
    df = pd.concat([df, new_record_df], ignore_index=True)
    
    # Lưu DataFrame vào file CSV
    df.to_csv("doanpython/data/weight_change_dataset.csv", index=False)
    
    return df
