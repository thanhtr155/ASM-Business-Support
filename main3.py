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
market_trends = market_trends. fillna('N/A')
customers = customers. fillna('N/A')
categories = categories.fillna('N/A')

# Convert date columns to datetime format
website_access_data['AccessDate'] = pd.to_datetime(website_access_data['AccessDate'])
transactions['TransactionDate'] = pd.to_datetime(transactions['TransactionDate'])

# Group the data by access date and count the page views
website_access_data['AccessDate'] = pd.to_datetime(website_access_data[ 'AccessDate'])
page_views_by_day = website_access_data.groupby(website_access_data['AccessDate'].dt.date). size()
page_views_by_month = website_access_data.groupby(website_access_data['AccessDate'].dt.strftime('%Y-%m')) .size()

# Create the plots
fig, (ax1, ax2) = plt.subplots( 2, 1, figsize=(12,8))

# Plot daily page views
ax1.plot(page_views_by_day.index, page_views_by_day.values)
ax1.set_title('Daily Website Page Views')
ax1.set_xlabel('Date')
ax1.set_ylabel('Page Views')

# Plot monthly page views
ax2.plot(page_views_by_month.index, page_views_by_month.values)
ax2.set_title('Monthly Website Page Views')
ax2. set_xlabel ( 'Month')
ax2.set_ylabel('Page Views')

plt.tight_layout ()
plt.show()

