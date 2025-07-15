import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Read the dataset
df = pd.read_csv('supermarket_sales.csv')
df.columns = df.columns.str.strip()  # Clean column names

# Create folder for charts
os.makedirs('charts', exist_ok=True)

# Bar Chart: Total Sales per Product Line
df.groupby('Product line')['Sales'].sum().sort_values().plot(kind='barh', color='skyblue')
plt.title('Total Sales by Product Line')
plt.xlabel('Total Sales')
plt.savefig('charts/product_line_sales.png')
plt.close()

# Pie Chart: Sales Share by City
df.groupby('City')['Sales'].sum().plot(kind='pie', autopct='%1.1f%%')
plt.title('Sales by City')
plt.ylabel('')
plt.savefig('charts/city_sales.png')
plt.close()

# Line Plot: Revenue Over Time
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df.groupby('Date')['Sales'].sum().plot(marker='o')
plt.title('Total Revenue Over Time')
plt.ylabel('Total Sales')
plt.savefig('charts/revenue_over_time.png')
plt.close()

# Payment Method Distribution
df['Payment'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title('Payment Methods')
plt.ylabel('')
plt.savefig('charts/payment_methods.png')
plt.close()

# Heatmap: Correlation Matrix (Correct Columns)
plt.figure(figsize=(6, 4))
sns.heatmap(df[['Sales', 'Tax 5%', 'cogs', 'gross income', 'Quantity']].corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.savefig('charts/heatmap.png')
plt.close()

# Rating Histogram
df['Rating'].plot(kind='hist', bins=10, color='lightgreen')
plt.title('Customer Rating Distribution')
plt.xlabel('Rating')
plt.savefig('charts/rating_histogram.png')
plt.close()

print('✅ All charts saved in "charts" folder.')

