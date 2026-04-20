import pandas as pd


if __name__ == "__main__":
    fsi = pd.read_csv("FSI_standardized.csv")
    features = pd.read_csv("features_updated.csv")

    fsi.columns = fsi.columns.str.strip()
    features.columns = features.columns.str.strip()

    df = pd.merge(fsi, features, on=["Country", "Year"], how="left")
    df = df.sort_values(by=["Country", "Year"]).reset_index(drop=True)

    feature_cols = [
        "GDP_per_capita",
        "Internet_users_percent",
        "Life_expectancy",
        "Military_expenditure_percent",
    ]

    df[feature_cols] = df.groupby("Country")[feature_cols].ffill()
    df[feature_cols] = df.groupby("Country")[feature_cols].bfill()

    for col in feature_cols:
        df[col] = df[col].fillna(df[col].median())

    if "Change from Previous Year" in df.columns:
        df = df.drop(columns=["Change from Previous Year"])
    if "Change from Previous Year" in fsi.columns:
        fsi = fsi.drop(columns=["Change from Previous Year"])

    fsi.to_csv("fsi_weka_ready.csv", index=False)
    df.to_csv("fsi_combined_weka_ready.csv", index=False)

    print("✅ FINAL DATASETS READY")
    print("\nFinal shape:", df.shape)
    print("Countries:", df["Country"].nunique())
    print("Duplicates:", df.duplicated(subset=["Country", "Year"]).sum())
    print("\nMissing values:\n", df.isnull().sum())
