import pandas as pd

# 1. Load the dataset
file_path = "data/customer_reviews.csv"
print(f"Loading dataset from '{file_path}'...")
df = pd.read_csv(file_path)

# 2. Inspect initial dimensions
print(f"\n--- Initial Dataset Info ---")
print(f"Total Rows: {df.shape[0]}")
print(f"Total Columns: {df.shape[1]}")

# 3. Check for missing values
print(f"\n--- Checking for Missing Values ---")
missing_values = df.isnull().sum()
print(missing_values)

# 4. Check for duplicate rows
print(f"\n--- Checking for Duplicates ---")
duplicates_count = df.duplicated(subset=['review_id']).sum()
print(f"Duplicate review IDs found: {duplicates_count}")

# 5. Check and fix data types
print(f"\n--- Checking Data Types ---")
print(df.dtypes)

# Convert date column to actual datetime objects for time-series analysis later
df['date'] = pd.to_datetime(df['date'])

# Ensure ratings are integers
df['rating'] = df['rating'].astype(int)

# 6. Clean review text (strip whitespace)
df['review_text'] = df['review_text'].str.strip()

# 7. Save the cleaned dataset
cleaned_file_path = "data/cleaned_customer_reviews.csv"
df.to_csv(cleaned_file_path, index=False)
print(f"\nData cleaning complete! Cleaned dataset saved to '{cleaned_file_path}'.")