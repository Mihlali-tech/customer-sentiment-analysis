import pandas as pd

# 1. Load the sentiment dataset
file_path = "data/sentiment_customer_reviews.csv"
df = pd.read_csv(file_path)

total_reviews = len(df)

print("=== OVERALL METRICS ===")
print(f"Total Reviews: {total_reviews}")
print(f"Overall Average Rating: {df['rating'].mean():.2f} / 5.0")

# 2. Sentiment Counts & Percentages
sentiment_counts = df['sentiment'].value_counts()
sentiment_pcts = (sentiment_counts / total_reviews) * 100

print("\n=== SENTIMENT BREAKDOWN ===")
for sentiment, count in sentiment_counts.items():
    pct = sentiment_pcts[sentiment]
    print(f"{sentiment}: {count} reviews ({pct:.1f}%)")

# 3. Sentiment & Rating by Product Category
print("\n=== PERFORMANCE BY PRODUCT CATEGORY ===")
category_summary = df.groupby('product_category').agg(
    total_reviews=('review_id', 'count'),
    avg_rating=('rating', 'mean'),
    avg_sentiment_score=('sentiment_score', 'mean')
).reset_index().sort_values(by='avg_rating', ascending=False)

print(category_summary.to_string(index=False))

# 4. Sentiment by Customer Type
print("\n=== SENTIMENT BY CUSTOMER TYPE ===")
customer_sentiment = pd.crosstab(df['customer_type'], df['sentiment'], normalize='index') * 100
print(customer_sentiment.round(1))