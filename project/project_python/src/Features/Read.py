import pandas as pd

def read():
    csv_path = "project_python/data/laptop_price - dataset.csv"
    df = pd.read_csv(csv_path)
    return df