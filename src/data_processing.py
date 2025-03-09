import pandas as pd

def load_data(filepath):
    """Load dataset from a given filepath."""
    return pd.read_csv(filepath)

def clean_data(df):
    """Perform basic data cleaning such as handling missing values and duplicates."""
    df.drop_duplicates(inplace=True)
    df.fillna(method='ffill', inplace=True)
    return df

def save_data(df, filepath):
    """Save processed data to a given filepath."""
    df.to_csv(filepath, index=False)

if __name__ == "__main__":
    raw_data = load_data("data/raw/supplier_data.csv")
    cleaned_data = clean_data(raw_data)
    save_data(cleaned_data, "data/processed/supplier_data_cleaned.csv")
