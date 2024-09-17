import pandas as pd
from pymongo import MongoClient 

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['product_db']
collection = db['products']

# Read CSV file
df = pd.read_csv('sample_data.csv')

# Convert CSV data to dictionary and insert into MongoDB
data = df.to_dict(orient='records')
collection.insert_many(data)

print("CSV data successfully loaded into MongoDB.")
