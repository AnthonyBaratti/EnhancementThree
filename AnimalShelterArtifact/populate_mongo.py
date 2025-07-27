import pandas as pd
from pymongo import MongoClient

#Load CSV into a DataFrame
df = pd.read_csv("aac_shelter_outcomes.csv")

#Connect to MongoDB (local instance, default port)
client = MongoClient("mongodb://localhost:27017/")

#Define the database and collection
db = client["AAC"]
collection = db["animals"]

#Clear existing documents to prevent double loading.
collection.delete_many({})

#Insert data into MongoDB
data = df.to_dict(orient="records")
collection.insert_many(data)

#Confirm records loaded.
print(f"Inserted {len(data)} records into AAC.animals")