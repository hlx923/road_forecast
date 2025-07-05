import pandas as pd

def load_data(path):
    # ... existing code ...
    df = pd.read_csv(path)
    return df

def add_time_features(df):
    # ... existing code ...
    df['hour'] = pd.to_datetime(df['timestamp']).dt.hour
    df['weekday'] = pd.to_datetime(df['timestamp']).dt.weekday
    # ... existing code ...
    return df

def add_lag_features(df, lag_steps=[1,2,3]):
    # ... existing code ...
    for lag in lag_steps:
        df[f'flow_lag_{lag}'] = df.groupby('road_id')['flow'].shift(lag)
    return df

# ... existing code ...