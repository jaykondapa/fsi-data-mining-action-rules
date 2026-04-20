import pandas as pd


if __name__ == "__main__":
    fsi = pd.read_csv("FSI_final.csv")
    features = pd.read_csv("features.csv")

    fsi.columns = fsi.columns.str.strip()
    features.columns = features.columns.str.strip()

    fsi_mapping = {
        "Cabo Verde": "Cape Verde",
        "Czechia": "Czech Republic",
        "Kyrgyz Republic": "Kyrgyzstan",
        "North Macedonia": "Macedonia",
        "Swaziland": "Eswatini",
        "Slovak Republic": "Slovakia",
    }
    fsi["Country"] = fsi["Country"].replace(fsi_mapping)

    features_mapping = {
        "Bahamas, The": "Bahamas",
        "Egypt, Arab Rep.": "Egypt",
        "Gambia, The": "Gambia",
        "Iran, Islamic Rep.": "Iran",
        "Micronesia, Fed. Sts.": "Micronesia",
        "Russian Federation": "Russia",
        "Somalia, Fed. Rep.": "Somalia",
        "Syrian Arab Republic": "Syria",
        "Yemen, Rep.": "Yemen",
        "Viet Nam": "Vietnam",
        "Cabo Verde": "Cape Verde",
        "Congo, Dem. Rep.": "Congo Democratic Republic",
        "Congo, Rep.": "Congo Republic",
        "Korea, Rep.": "South Korea",
        "Korea, Dem. People's Rep.": "North Korea",
        "Czechia": "Czech Republic",
        "North Macedonia": "Macedonia",
        "Turkiye": "Turkey",
        "Lao PDR": "Laos",
        "Guinea-Bissau": "Guinea Bissau",
        "Kyrgyz Republic": "Kyrgyzstan",
        "Slovak Republic": "Slovakia",
        "Venezuela, RB": "Venezuela",
    }
    features["Country"] = features["Country"].replace(features_mapping)

    features = features[features["Country"].isin(fsi["Country"])]
    features = features.drop_duplicates(subset=["Country", "Year"])
    fsi = fsi.drop_duplicates(subset=["Country", "Year"])

    features.to_csv("features_updated.csv", index=False)
    fsi.to_csv("FSI_standardized.csv", index=False)

    print("✅ FINAL CLEAN FILES READY")
    print("FSI countries:", fsi["Country"].nunique())
    print("Features countries:", features["Country"].nunique())
