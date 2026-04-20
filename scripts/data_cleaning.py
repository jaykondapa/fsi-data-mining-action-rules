import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    return df

def clean_data(df):
    df = df.dropna()
    df = df.drop_duplicates()
    return df

if __name__ == "__main__":
    df = load_data("fsi_dataset.csv")
    df_clean = clean_data(df)
    df_clean.to_csv("fsi_cleaned.csv", index=False)
