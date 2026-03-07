import argparse
import os
import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.model_selection import train_test_split

def train_model(args):
    # 1. Load CSV data from GCS
    print(f"Loading data from: {args.data_path}")
    df = pd.read_csv(args.data_path)

    # 2. Define Features and Target
    # features are f_0 to f_94
    feature_cols = [f'f_{i}' for i in range(95)]
    target_col = 'computed_total_charge'

    X = df[feature_cols].values
    y = df[target_col].values

    # 3. 70-15-15 Split
    X_train, X_rem, y_train, y_rem = train_test_split(
        X, y, test_size=0.30, random_state=42
    )
    
    X_val, X_test, y_val, y_test = train_test_split(
        X_rem, y_rem, test_size=0.50, random_state=42
    )

    # 4. Train XGBoost
    model = xgb.XGBRegressor(
        objective='reg:squarederror',
        n_estimators=1000,
        learning_rate=0.05,
        max_depth=6,
        subsample=0.8,
        early_stopping_rounds=20  
    )

    model.fit(
        X_train, y_train,
        eval_set=[(X_val, y_val)],
        verbose=100  # Prints progress every 100 rounds
    )

    # 5. Evaluate
    score = model.score(X_test, y_test)
    print(f"Test R2 Score: {score}")

        
    # 6. Save and Upload Model
    model_output_uri = os.environ.get('AIP_MODEL_DIR')
    local_path = 'model.bst' 
    model.save_model(local_path)

    if model_output_uri:
        # Explicitly define the full destination path
        gcs_path = os.path.join(model_output_uri, local_path)
        print(f"Uploading model to: {gcs_path}")
        os.system(f'gsutil cp {local_path} {gcs_path}')
    else:
        print("AIP_MODEL_DIR not found, saved locally only.")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data-path', type=str, required=True)
    args = parser.parse_args()
    train_model(args)