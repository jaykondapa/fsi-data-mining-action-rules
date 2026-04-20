import pandas as pd


def categorize_fsi(score: float) -> str:
    if pd.isna(score):
        return None
    if score < 30:
        return "Very Sustainable"
    elif score < 50:
        return "Sustainable"
    elif score < 70:
        return "Stable"
    elif score < 90:
        return "Warning"
    elif score < 100:
        return "Alert"
    else:
        return "Very High Alert"


def load_and_fix(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    df.columns = df.columns.str.strip()

    if "Year" in df.columns:
        df["Year"] = pd.to_datetime(df["Year"], errors="coerce").dt.year

    if "Total" in df.columns:
        df = df.rename(columns={"Total": "FSI"})

    if "Rank" in df.columns:
        df = df.drop(columns=["Rank"])

    return df


if __name__ == "__main__":
    fsi_2019 = load_and_fix("fsi-2019.csv")
    fsi_2020 = load_and_fix("fsi-2020.csv")
    fsi_2021 = load_and_fix("fsi-2021.csv")

    df = pd.concat([fsi_2019, fsi_2020, fsi_2021], ignore_index=True)
    df = df.drop_duplicates(subset=["Country", "Year"])
    df = df.sort_values(by=["Country", "Year"]).reset_index(drop=True)

    df["FSI_Category"] = df["FSI"].apply(categorize_fsi)

    cols = list(df.columns)
    cols.remove("FSI_Category")
    fsi_idx = cols.index("FSI")
    cols.insert(fsi_idx + 1, "FSI_Category")
    df = df[cols]

    df.to_csv("FSI_final.csv", index=False)

    print("✅ FSI_final.csv READY")
    print(df[["Country", "Year", "FSI", "FSI_Category"]].head())
    print("\nFSI category distribution:")
    print(df["FSI_Category"].value_counts())
