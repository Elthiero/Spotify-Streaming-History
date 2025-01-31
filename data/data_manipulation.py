# Data manipulation

# Importing packages/libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# Function to get csv data
def get_csv_data():
    csv_filename = "data/csv/spotify_history.csv"
    try:
        df = pd.read_csv(csv_filename)
    except FileNotFoundError:
        print(f"File {csv_filename} not found.")
        df = None
    return df

# Function to check missing values
def check_missing_values(df):
    number_of_missing_values = df.isnull().any().sum()
    if number_of_missing_values > 0:
        return True
    else:
        return False

def view_missing_values(df):
    missing_values_data = df.isnull().sum()
    plt.figure(figsize=(10, 8))
    plt.bar(missing_values_data.index, missing_values_data.values)
    plt.xlabel('Columns')
    plt.ylabel('Number of Missing Values')
    plt.title('Missing Values per Column')
    plt.xticks(rotation=55)
    plt.grid(True, linestyle='--', alpha=0.3)
    plt.show()    

# Function to fill missing values
def fill_missing_values(df, columns_name):
    # Fill missing values with unknown as value
    value = 'unknown'
    for column in columns_name:
        if df[column].isnull().any():
            df[column] = df[column].fillna(value)
    return df

def information_dataset(df):
    length = len(df)
    columns = (df.columns).tolist()
    dtypes = (df.dtypes).tolist()
    data_types = pd.DataFrame({
    "Column Name": df.columns,
    "Data Type": dtypes
})
    total_missing_values = df.isnull().any().sum()
    
    # return [length, columns, total_missing_values, data_types]
    return {'length': length, 'columns':columns, 
            'total_missing_values':total_missing_values, 
            'data_types':data_types}

def columns_for_analysis(df):
    df['ts'] = pd.to_datetime(df['ts'])
    df['hour'] = df['ts'].dt.hour
    df['day'] = df['ts'].dt.day
    df['month'] = df['ts'].dt.month
    df['year'] = df['ts'].dt.year
