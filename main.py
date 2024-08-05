import pandas as pd
# Read the "Website_Access_Data.csv" file
website_access_data = pd.read_csv('Website_Access_Data.csv')
print(website_access_data.head())

# Read the "transaction.csv" file
transactions = pd.read_csv('transaction.csv')
print(transactions.head())

# Read the "products.csv" file
products = pd.read_csv('products.csv')
print(products.head())

# Read the "Market_Trend.csv" file
market_trends = pd.read_csv('Market_Trend.csv')
print(market_trends.head())

# Read the "customer.csv" file
customers = pd.read_csv('customer.csv')
print(customers.head())

# Read the "Categories.csv" file
categories = pd.read_csv('Categories.csv')
print(categories.head())

# Handle blank data
website_access_data = website_access_data.fillna(0)
transactions = transactions.fillna(0)
products = products.fillna('N/A')
market_trends = market_trends.fillna('N/A')
customers = customers.fillna('N/A')
categories = categories.fillna('N/A')

# Handle error data
try:
    website_access_data['AccessDate'] = pd.to_datetime(website_access_data['AccessDate'])
except ValueError:
    website_access_data['AccessDate'] = pd.to_datetime('1900-01-01')

try:
    transactions['TransactionDate'] = pd.to_datetime(transactions['TransactionDate'])
except ValueError:
    transactions['TransactionDate'] = pd.to_datetime('1900-01-01')

try:
    products['UnitPrice'] = pd.to_numeric(products['UnitPrice'], errors='coerce')
except ValueError:
    products['UnitPrice'] = 0

try:
    market_trends['Q3_2023_Trend'] = pd.to_numeric(market_trends['Q3_2023_Trend'], errors='coerce')
    market_trends['Q4_2023_Trend'] = pd.to_numeric(market_trends['Q4_2023_Trend'], errors='coerce')
    market_trends['Q1_2024_Trend'] = pd.to_numeric(market_trends['Q1_2024_Trend'], errors='coerce')
    market_trends['Q2_2024_Trend'] = pd.to_numeric(market_trends['Q2_2024_Trend'], errors='coerce')
except ValueError:
    market_trends['Q3_2023_Trend'] = 0
    market_trends['Q4_2023_Trend'] = 0
    market_trends['Q1_2024_Trend'] = 0
    market_trends['Q2_2024_Trend'] = 0

try:
    customers['PhoneNumber'] = customers['PhoneNumber'].str.replace('+', '', regex=False)
except AttributeError:
    customers['PhoneNumber'] = '0'

# Check for any remaining NaN values
print(website_access_data.isnull().sum())
print(transactions.isnull().sum())
print(products.isnull().sum())
print(market_trends.isnull().sum())
print(customers.isnull().sum())
print(categories.isnull().sum())


