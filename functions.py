import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler


# Function to clean the 'Age' column by categorizing ages into groups
def clean_age_column(data):
    data['AgeGroup'] = pd.cut(data['age'], bins=[0, 18, 35, 50, 65, 100], labels=[0, 1, 2, 3, 4])
    data['AgeGroup'] = data['AgeGroup'].astype('int64') 
    data.drop(columns=["age"], inplace=True)

    return data


# Function to standardize the features of the training and test datasets
def Standardizer(X_train, X_test):
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    return X_train_scaled, X_test_scaled


# Function to normalize the features of the training and test datasets
def Normalizer(X_train, X_test):
    normalizer = MinMaxScaler()
    X_train_norm = normalizer.fit_transform(X_train)
    X_test_norm = normalizer.transform(X_test)

    return X_train_norm, X_test_norm
