import pandas as pd
from pymongo import MongoClient

# Step 1: Load CSV into a DataFrame
df = pd.read_csv("aac_shelter_outcomes.csv")

# Step 2: Connect to MongoDB (local instance, default port)
client = MongoClient("mongodb://localhost:27017/")

# Step 3: Define the database and collection
db = client["AAC"]
collection = db["animals"]

# Step 4: Optional - Clear existing documents
collection.delete_many({})

# Step 5: Insert data into MongoDB
data = df.to_dict(orient="records")
collection.insert_many(data)

print(f"✅ Inserted {len(data)} records into AAC.animals")