import pandas as pd

def read():
    csv_path = "doanpython/data/weight_change_dataset.csv"
    df = pd.read_csv(csv_path)
    return df