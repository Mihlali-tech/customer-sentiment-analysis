import pandas as pd
from textblob import TextBlob

# 1. Load the cleaned dataset
file_path = "data/cleaned_customer_reviews.csv"
print(f"Loading dataset from '{file_path}'...")
df = pd.read_csv(file_path)

# 2. Function to compute sentiment polarity using TextBlob
def get_sentiment(text):
    analysis = TextBlob(str(text))
    polarity = analysis.sentiment.polarity
    
    # Classify based on polarity thresholds
    if polarity > 0.1:
        return 'Positive', round(polarity, 2)
    elif polarity < -0.1:
        return 'Negative', round(polarity, 2)
    else:
        return 'Neutral', round(polarity, 2)

# 3. Apply sentiment analysis to review text
print("Running sentiment analysis on customer reviews...")
sentiments = df['review_text'].apply(get_sentiment)

# Unpack the results into two new columns
df['sentiment'] = [s[0] for s in sentiments]
df['sentiment_score'] = [s[1] for s in sentiments]

# 4. Display summary of sentiments
print("\n--- Sentiment Distribution Summary ---")
print(df['sentiment'].value_counts())

# 5. Save the updated dataset with sentiment columns
output_file = "data/sentiment_customer_reviews.csv"
df.to_csv(output_file, index=False)
print(f"\nSentiment analysis complete! Updated dataset saved to '{output_file}'.")

# Show first 3 rows with sentiment
print("\nFirst 3 rows with sentiment columns:")
print(df[['review_id', 'rating', 'sentiment', 'sentiment_score', 'review_text']].head(3))