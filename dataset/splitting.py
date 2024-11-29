import pandas as pd
from sklearn.model_selection import train_test_split

# Load the dataset
data = pd.read_csv("Splitting.csv")  # Replace with the path to your dataset

# Define the percentage for the test split (e.g., 20% for test data)
test_size_percentage = 0.65

# Split the data into test and unlabeled datasets
test_data, unlabeled_data = train_test_split(data, test_size=test_size_percentage, random_state=42)

# Save the split datasets into separate CSV files
test_data.to_csv("Test.csv", index=False)
unlabeled_data.to_csv("unlabeled.csv", index=False)
