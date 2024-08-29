import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import streamlit as st

# Loading the dataset
df = pd.read_csv(r'C:\Users\USER\Downloads\Expresso_churn_dataset.csv')
# Display general information about the dataset
print(df.info())
# Display general information about the dataset
print(df.info())

# Display summary statistics
print(df.describe())


#from ydata_profiling import ProfileReport
#ProfileReport(df)

# Check for missing values
print(df.isnull().sum())

# Handle missing values (example: filling with median for numerical features)
for col in df.select_dtypes(include=[np.number]).columns:
    df[col].fillna(df[col].median(), inplace=True)

# For categorical features, filling missing values with the mode
for col in df.select_dtypes(include=[object]).columns:
    df[col].fillna(df[col].mode()[0], inplace=True)

    # Check for duplicates
print(f"Number of duplicate rows: {df.duplicated().sum()}")

# Remove duplicates if they exist
df.drop_duplicates(inplace=True)

# Identify and handle outliers using IQR method
for col in df.select_dtypes(include=[np.number]).columns:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    outliers = df[(df[col] < (Q1 - 1.5 * IQR)) | (df[col] > (Q3 + 1.5 * IQR))]
    if not outliers.empty:
        print(f"Handling outliers in column: {col}")
# For simplicity, let's clip the outliers to the 1.5*IQR range
        df[col] = np.clip(df[col], Q1 - 1.5 * IQR, Q3 + 1.5 * IQR)

        # Reduce cardinality for high cardinality categorical features
def reduce_cardinality(series, threshold=0.01):
    freq = series.value_counts(normalize=True)
    other_categories = freq[freq < threshold].index
    return series.apply(lambda x: 'Other' if x in other_categories else x)

# Select features and target
selected_features = ['REVENUE', 'FREQUENCE_RECH', 'MONTANT', 'CHURN']
X = df[selected_features]
y = df['CHURN']

# Encode categorical features using sparse data structures
categorical_features = df.select_dtypes(include=['object']).columns
df_sparse = pd.get_dummies(df, columns=categorical_features, drop_first=True, sparse=True)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


from sklearn.preprocessing import StandardScaler

scaler = StandardScaler(with_mean=False) 
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


# Initialize and train the classifier
clf = RandomForestClassifier()
clf.fit(X_train, y_train)

# Make predictions
y_pred = clf.predict(X_test)

# Evaluate the model
print('Accuracy:', accuracy_score(y_test, y_pred))
print('Classification Report:')
print(classification_report(y_test, y_pred))
print('Confusion Matrix:')
print(confusion_matrix(y_test, y_pred))


# Saving the model
import pickle
filename = "trained_model.sav"
pickle.dump(RandomForestClassifier, open(filename, "wb"))