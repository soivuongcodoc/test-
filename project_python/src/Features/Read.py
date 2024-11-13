import pandas as pd

def read():
    csv_path = "project_python/laptop_price - dataset.csv"
    df = pd.read_csv(csv_path)
    return df