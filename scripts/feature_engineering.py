import pandas as pd

def categorize_column(series, bins, labels):
    return pd.cut(series, bins=bins, labels=labels, include_lowest=True)

def create_categories(df):
    df['GDP_Category'] = categorize_column(df['GDP'], bins=3, labels=['Low','Medium','High'])
    df['Internet_Category'] = categorize_column(df['Internet'], bins=3, labels=['Low','Medium','High'])
    df['Life_Expectancy_Category'] = categorize_column(df['Life_Expectancy'], bins=3, labels=['Low','Medium','High'])
    df['Military_Expenditure_Category'] = categorize_column(df['Military'], bins=3, labels=['Low','Medium','High'])
    return df

if __name__ == "__main__":
    df = pd.read_csv("fsi_cleaned.csv")
    df_cat = create_categories(df)
    df_cat.to_csv("fsi_categorized.csv", index=False)
