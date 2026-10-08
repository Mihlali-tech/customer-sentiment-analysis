import os
import random
import pandas as pd
from datetime import datetime, timedelta

# Set a random seed so your generated data is reproducible
random.seed(42)

# Define categories, customer types, and sample review templates
categories = ['Electronics', 'Home & Kitchen', 'Apparel', 'Beauty', 'Books']
customer_types = ['New', 'Regular', 'VIP']

# Sample review pools for different sentiments
positive_templates = [
    "Absolutely love this product! Exceeded my expectations.",
    "Great quality and fast shipping. Highly recommend!",
    "Fantastic customer service and works like a charm.",
    "Very happy with my purchase, worth every penny.",
    "Top-notch quality. Will definitely buy again!"
]

neutral_templates = [
    "It's okay, nothing special. Does the job.",
    "Average product for the price. Delivery took a bit long.",
    "Decent quality, but packaging was slightly damaged.",
    "Met basic expectations, though I expected a bit more durability.",
    "The item is fine, but instructions were confusing."
]

negative_templates = [
    "Terrible quality broke after two days of use.",
    "Very disappointed. Customer support was unhelpful.",
    "Not worth the money at all. Stopped working immediately.",
    "Horrible experience, delayed shipping and poor item condition.",
    "Do not buy this! Total waste of money."
]

data = []
start_date = datetime(2025, 1, 1)

for i in range(1, 301):
    review_id = f"REV-{1000 + i}"
    category = random.choice(categories)
    customer_type = random.choice(customer_types)
    
    # Randomly skew ratings to create realistic variation
    # Let's make ratings correlate roughly with sentiment templates
    sentiment_roll = random.random()
    
    if sentiment_roll < 0.55:  # 55% Positive
        rating = random.choices([4, 5], weights=[0.4, 0.6])[0]
        review_text = random.choice(positive_templates)
    elif sentiment_roll < 0.80:  # 25% Neutral
        rating = random.choices([2, 3], weights=[0.3, 0.7])[0]
        review_text = random.choice(neutral_templates)
    else:  # 20% Negative
        rating = random.choices([1, 2], weights=[0.7, 0.3])[0]
        review_text = random.choice(negative_templates)
        
    # Generate random date within the past year
    random_days = random.randint(0, 365)
    review_date = start_date + timedelta(days=random_days)
    
    data.append({
        "review_id": review_id,
        "review_text": review_text,
        "rating": rating,
        "product_category": category,
        "date": review_date.strftime("%Y-%m-%d"),
        "customer_type": customer_type
    })

# Convert to a Pandas DataFrame
df_reviews = pd.DataFrame(data)

# Create the 'data' directory if it doesn't exist
os.makedirs("data", exist_ok=True)

# Save the DataFrame to a CSV file
file_path = "data/customer_reviews.csv"
df_reviews.to_csv(file_path, index=False)

print(f"Successfully generated {len(df_reviews)} reviews and saved to '{file_path}'.")
print("\nFirst 3 rows of the dataset:")
print(df_reviews.head(3))