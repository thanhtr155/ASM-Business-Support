import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV files
website_access_data = pd.read_csv('Website_Access_Data.csv')
transactions = pd.read_csv('transaction.csv')
products = pd.read_csv('products.csv')
market_trends = pd.read_csv('Market_Trend.csv')
customers = pd.read_csv('customer.csv')
categories = pd.read_csv('Categories.csv')

# Handle blank and error data
website_access_data = website_access_data.fillna(0)
transactions = transactions.fillna(0)
products = products.fillna('N/A')
market_trends = market_trends.fillna('N/A')
customers = customers.fillna('N/A')
categories = categories.fillna('N/A')

# Merge the transactions and products data
sales_data = pd.merge(transactions, products, on='ProductID', how='left')

# Calculate total sales and total amount by product ID
sales_by_product = sales_data.groupby('ProductID')[['Quantity', 'TotalAmount']].sum().reset_index()

# Create the bar plots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))

ax1.bar(sales_by_product['ProductID'], sales_by_product['Quantity'])
ax1.set_title('Total Quantity by Product ID')
ax1.set_xlabel('Product ID')
ax1.set_ylabel('Total Quantity')

ax2.bar(sales_by_product['ProductID'], sales_by_product['TotalAmount'])
ax2.set_title('Total Amount by Product ID')
ax2.set_xlabel('Product ID')
ax2.set_ylabel('Total Amount')

plt.tight_layout()
plt.show()