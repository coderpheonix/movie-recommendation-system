import pandas as pd
from config.db_config import movies_collection

# Load CSV from data folder
df = pd.read_csv("data/movies.csv")

# Drop duplicates and fill missing genres
df = df.drop_duplicates(subset=["movieId"])
df['genres'] = df['genres'].fillna('')

# Clear existing collection (safe reload)
movies_collection.delete_many({})

# Insert all movies into MongoDB
movies_collection.insert_many(df.to_dict("records"))

print("✅ Movies inserted into MongoDB successfully!")
