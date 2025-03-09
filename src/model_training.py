import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

def train_model(df):
    """Train a machine learning model to predict supplier risk."""
    X = df[['avg_delivery_delay', 'defect_ratio', 'transaction_consistency']]
    y = df['risk_category']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    joblib.dump(model, 'supplier_risk_model.pkl')
    print("Model trained and saved.")
    
if __name__ == "__main__":
    df = pd.read_csv("data/processed/supplier_data_with_features.csv")
    train_model(df)
