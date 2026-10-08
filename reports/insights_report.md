# Customer Sentiment Analysis — Insights Report

## 1. Executive Summary
This report provides a comprehensive analysis of customer feedback across 300 synthetic reviews collected over a one-year period. Using Python, Pandas, and TextBlob NLP sentiment modeling, we evaluated customer satisfaction, rating distributions, and product category performance. Overall, customer sentiment is predominantly **positive (64.3%)**, with an average rating of **3.44 / 5.0**. However, notable pockets of negative feedback (**16.7%**) highlight specific areas for operational and product improvement.

## 2. Project Objective
The primary objective of this project is to transform raw, unstructured customer review text into actionable business insights by:
* Quantifying overall customer satisfaction and sentiment breakdown.
* Identifying top-performing and underperforming product categories.
* Uncovering key drivers of positive and negative customer experiences.
* Delivering evidence-based recommendations to leadership.

## 3. Dataset
* **Total Records:** 300 customer reviews.
* **Columns:** `review_id`, `review_text`, `rating` (1–5), `product_category`, `date`, `customer_type`.
* **Customer Segments:** New, Regular, and VIP customers.
* **Data Nature:** Synthetic dataset designed to mirror realistic e-commerce feedback patterns.

## 4. Methodology
1. **Data Cleaning:** Inspected for null values and duplicates, standardized data types, and validated date formats.
2. **Exploratory Data Analysis (EDA):** Calculated summary statistics and generated distributions using Matplotlib and Seaborn.
3. **Sentiment Analysis:** Applied Natural Language Processing (TextBlob) to evaluate review polarity, classifying feedback into Positive, Neutral, and Negative categories.
4. **Interactive Dashboard:** Deployed a Streamlit web application for real-time filtering and data exploration.

## 5. Key Findings
* **Overall Rating:** 3.44 out of 5.0 stars.
* **Sentiment Breakdown:**
  * **Positive:** 193 reviews (64.3%)
  * **Neutral:** 57 reviews (19.0%)
  * **Negative:** 50 reviews (16.7%)
* **Customer Loyalty Insight:** VIP customers demonstrated the highest positive sentiment (**71.3%**), whereas Regular customers reported the highest negative feedback rate (**23.5%**).

## 6. Category Performance Analysis
* **Top Performers:** 
  * **Home & Kitchen:** Highest average rating (**3.65 / 5.0**) and highest average sentiment score (**0.26**).
  * **Apparel:** Strong performance with an average rating of **3.62 / 5.0**.
* **Underperforming Categories:**
  * **Books:** Lowest average rating (**3.16 / 5.0**) and lowest sentiment score (**0.09**), indicating customer dissatisfaction regarding quality, packaging, or descriptions.
  * **Electronics:** Struggling with lower satisfaction (**3.37 / 5.0**), frequently prone to durability complaints.

## 7. Business Recommendations
1. **Investigate Supplier Quality for Books:** Audit book suppliers and product descriptions to address the root causes of lower ratings.
2. **Retain Regular Customers:** Since Regular customers exhibit a higher negative rate (23.5%), introduce a targeted loyalty program or satisfaction check-in to bridge the gap between New and VIP experiences.
3. **Enhance Electronics Quality Control:** Address recurring negative themes around item reliability in electronics.
4. **Leverage Positive Momentum:** Scale successful marketing practices from Home & Kitchen and Apparel to underperforming categories.

## 8. Limitations
* **Synthetic Data:** Findings reflect modeled distributions rather than live commercial transactions.
* **NLP Lexicon Limitations:** TextBlob relies on rule-based lexicons which can occasionally misinterpret sarcasm, irony, or domain-specific slang.
* **Sample Size:** 300 reviews provide a solid portfolio baseline, but production environments require thousands of records.

## 9. Conclusion
The Customer Sentiment Analysis dashboard successfully demonstrates end-to-end data science capabilities—from data ingestion and cleaning to NLP modeling and interactive visualization. Addressing the identified pain points in Books and Electronics will drive significant improvements in overall customer retention.
