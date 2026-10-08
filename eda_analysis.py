import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set visual style for clean, professional charts
sns.set_theme(style="whitegrid")

# 1. Load the cleaned dataset
file_path = "data/cleaned_customer_reviews.csv"
print(f"Loading cleaned dataset from '{file_path}'...")
df = pd.read_csv(file_path)

# 2. Calculate summary statistics
print("\n--- Summary Statistics ---")
total_reviews = len(df)
avg_rating = df['rating'].mean()
print(f"Total Reviews: {total_reviews}")
print(f"Overall Average Rating: {avg_rating:.2f} / 5.0")

print("\nRating Breakdown:")
print(df['rating'].value_counts().sort_index())

print("\nReviews per Product Category:")
print(df['product_category'].value_counts())

print("\nAverage Rating by Product Category:")
print(df.groupby('product_category')['rating'].mean().round(2))

# 3. Create 'images/charts' directory if it doesn't exist
os.makedirs("images/charts", exist_ok=True)

# 4. Generate Visualizations
print("\nGenerating and saving charts...")

# Chart 1: Rating Distribution
plt.figure(figsize=(8, 5))
ax = sns.countplot(data=df, x='rating', palette='Blues_r', hue='rating', legend=False)
plt.title("Customer Rating Distribution", fontsize=14, fontweight='bold', pad=15)
plt.xlabel("Rating (Stars)", fontsize=12)
plt.ylabel("Number of Reviews", fontsize=12)
for p in ax.patches:
    ax.annotate(f'{int(p.get_height())}', (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', xytext=(0, 5), textcoords='offset points')
plt.tight_layout()
plt.savefig("images/charts/rating_distribution.png", dpi=300)
plt.close()

# Chart 2: Reviews by Product Category
plt.figure(figsize=(10, 5))
ax = sns.countplot(data=df, y='product_category', order=df['product_category'].value_counts().index, palette='crest', hue='product_category', legend=False)
plt.title("Review Volume by Product Category", fontsize=14, fontweight='bold', pad=15)
plt.xlabel("Number of Reviews", fontsize=12)
plt.ylabel("Product Category", fontsize=12)
plt.tight_layout()
plt.savefig("images/charts/reviews_by_category.png", dpi=300)
plt.close()

# Chart 3: Average Rating by Product Category
plt.figure(figsize=(10, 5))
category_ratings = df.groupby('product_category')['rating'].mean().reset_index().sort_values(by='rating', ascending=False)
ax = sns.barplot(data=category_ratings, x='rating', y='product_category', palette='magma', hue='product_category', legend=False)
plt.title("Average Rating by Product Category", fontsize=14, fontweight='bold', pad=15)
plt.xlabel("Average Rating (1-5)", fontsize=12)
plt.ylabel("Product Category", fontsize=12)
plt.xlim(0, 5)
plt.tight_layout()
plt.savefig("images/charts/avg_rating_by_category.png", dpi=300)
plt.close()

print("EDA complete! 3 charts saved successfully in 'images/charts/'.")