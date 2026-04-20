import pandas as pd
import numpy as np


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


if __name__ == "__main__":
    df = pd.read_csv("fsi_combined_weka_ready.csv")
    df.columns = df.columns.str.strip()

    df["FSI_Category"] = df["FSI"].apply(categorize_fsi)

    fsi_indicator_cols = [
        "C1: Security Apparatus",
        "C2: Factionalized Elites",
        "C3: Group Grievance",
        "E1: Economy",
        "E2: Economic Inequality",
        "E3: Human Flight and Brain Drain",
        "P1: State Legitimacy",
        "P2: Public Services",
        "P3: Human Rights",
        "S1: Demographic Pressures",
        "S2: Refugees and IDPs",
        "X1: External Intervention",
    ]

    for col in fsi_indicator_cols:
        safe_name = (
            col.replace(":", "")
               .replace(" ", "_")
               .replace("-", "_")
               .replace("/", "_")
        )
        df[f"{safe_name}_Disc"] = pd.cut(
            df[col],
            bins=[-np.inf, 5, 8, np.inf],
            labels=["Low", "Medium", "High"],
            right=False,
        )

    df["GDP_Category"] = pd.cut(
        df["GDP_per_capita"],
        bins=[-np.inf, 10000, 30000, np.inf],
        labels=["Low", "Medium", "High"],
        right=False,
    )

    df["Internet_Category"] = pd.cut(
        df["Internet_users_percent"],
        bins=[-np.inf, 33, 67, np.inf],
        labels=["Low", "Medium", "High"],
        right=False,
    )

    df["Life_Expectancy_Category"] = pd.cut(
        df["Life_expectancy"],
        bins=[-np.inf, 60, 75, np.inf],
        labels=["Low", "Medium", "High"],
        right=False,
    )

    df["Military_Expenditure_Category"] = pd.cut(
        df["Military_expenditure_percent"],
        bins=[-np.inf, 1.5, 3.5, np.inf],
        labels=["Low", "Medium", "High"],
        right=False,
    )

    disc_indicator_cols = [c for c in df.columns if c.endswith("_Disc")]

    lisp_cols = [
        "Country",
        "FSI_Category",
    ] + disc_indicator_cols + [
        "GDP_Category",
        "Internet_Category",
        "Life_Expectancy_Category",
        "Military_Expenditure_Category",
    ]

    lisp_df = df[lisp_cols].copy()
    lisp_df.to_csv("fsi_for_lispminer_FINAL.csv", index=False)

    print("✅ FINAL LISP DATASET READY")
    print("\nFSI_Category distribution:")
    print(df["FSI_Category"].value_counts(dropna=False))
    print("\nPreview:")
    print(lisp_df.head())
