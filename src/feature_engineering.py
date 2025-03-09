import pandas as pd

def create_features(df):
    """Generate new features for supplier risk analysis."""
    df['avg_delivery_delay'] = df['delivery_days'] - df['expected_delivery_days']
    df['defect_ratio'] = df['defective_items'] / df['total_items']
    df['transaction_consistency'] = df.groupby('supplier_id')['total_items'].transform('std')
    return df

if __name__ == "__main__":
    df = pd.read_csv("data/processed/supplier_data_cleaned.csv")
    df = create_features(df)
    df.to_csv("data/processed/supplier_data_with_features.csv", index=False)
