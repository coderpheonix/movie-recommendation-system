# config/db_config.py
from pymongo import MongoClient

# Local MongoDB URI
MONGO_URI = "mongodb://localhost:27017/"

# Connect to MongoDB
client = MongoClient(MONGO_URI)

# Create/use database
db = client["movieDB"]

# Movies collection
movies_collection = db["movies"]
