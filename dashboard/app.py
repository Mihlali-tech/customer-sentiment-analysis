import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set page configuration
st.set_page_config(
    page_title="Customer Sentiment Dashboard",
    page_icon="📊",
    layout="wide"
)

# Load data with caching for performance
@st.cache_data
def load_data():
    return pd.read_csv("data/sentiment_customer_reviews.csv")

df = load_data()

# App Title & Description
st.title("📊 Customer Sentiment Analysis & Insights Dashboard")
st.markdown("Explore customer feedback patterns, product category performance, and sentiment breakdowns across reviews.")

# --- SIDEBAR FILTERS ---
st.sidebar.header("🔍 Filter Dashboard")

# Category Filter
selected_category = st.sidebar.selectbox(
    "Select Product Category",
    options=["All"] + list(df['product_category'].unique())
)

# Customer Type Filter
selected_customer_type = st.sidebar.selectbox(
    "Select Customer Type",
    options=["All"] + list(df['customer_type'].unique())
)

# Sentiment Filter
selected_sentiment = st.sidebar.selectbox(
    "Select Sentiment",
    options=["All"] + list(df['sentiment'].unique())
)

# Apply Filters
filtered_df = df.copy()
if selected_category != "All":
    filtered_df = filtered_df[filtered_df['product_category'] == selected_category]
if selected_customer_type != "All":
    filtered_df = filtered_df[filtered_df['customer_type'] == selected_customer_type]
if selected_sentiment != "All":
    filtered_df = filtered_df[filtered_df['sentiment'] == selected_sentiment]

# --- KPI METRIC CARDS ---
total_revs = len(filtered_df)
avg_rat = filtered_df['rating'].mean() if total_revs > 0 else 0
pos_pct = (len(filtered_df[filtered_df['sentiment'] == 'Positive']) / total_revs * 100) if total_revs > 0 else 0
neg_pct = (len(filtered_df[filtered_df['sentiment'] == 'Negative']) / total_revs * 100) if total_revs > 0 else 0

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Reviews", total_revs)
col2.metric("Avg Rating", f"{avg_rat:.2f} / 5.0")
col3.metric("Positive Sentiment", f"{pos_pct:.1f}%")
col4.metric("Negative Sentiment", f"{neg_pct:.1f}%")

st.markdown("---")

# --- CHARTS SECTION ---
row1_col1, row1_col2 = st.columns(2)

with row1_col1:
    st.subheader("Sentiment Distribution")
    if total_revs > 0:
        sentiment_counts = filtered_df['sentiment'].value_counts()
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', startangle=90, colors=['#4CAF50', '#FFC107', '#F44336'])
        ax.axis('equal')
        st.pyplot(fig)
    else:
        st.warning("No data available for selected filters.")

with row1_col2:
    st.subheader("Average Rating by Category")
    if total_revs > 0:
        cat_ratings = filtered_df.groupby('product_category')['rating'].mean().reset_index()
        fig, ax = plt.subplots(figsize=(6, 4))
        sns.barplot(data=cat_ratings, x='rating', y='product_category', palette='viridis', ax=ax, hue='product_category', legend=False)
        ax.set_xlim(0, 5)
        ax.set_xlabel("Average Rating")
        ax.set_ylabel("Category")
        st.pyplot(fig)
    else:
        st.warning("No data available for selected filters.")

# --- RAW DATA TABLE ---
st.subheader("📋 Filtered Customer Review Data")
st.dataframe(filtered_df[['review_id', 'date', 'product_category', 'customer_type', 'rating', 'sentiment', 'review_text']], width='stretch')