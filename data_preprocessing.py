import pandas as pd

def load_data():
    df = pd.read_csv("C:\\Users\\Mohammed Yunus\\Datascience\\customer-segmentation-analysis\\data\\Mall_Customers (2).csv")
    X = df.iloc[:, [3, 4]].values
    return df, X