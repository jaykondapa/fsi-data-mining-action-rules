import pandas as pd

def prepare_for_lispminer(df):
    cols = [
        'Country',
        'GDP_Category',
        'Internet_Category',
        'Life_Expectancy_Category',
        'Military_Expenditure_Category',
        'FSI_Category'
    ]
    return df[cols]

if __name__ == "__main__":
    df = pd.read_csv("fsi_categorized.csv")
    df_final = prepare_for_lispminer(df)
    df_final.to_csv("fsi_for_lispminer_FINAL.csv", index=False)
