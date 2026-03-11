from pymongo import MongoClient
import os

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")

client = MongoClient(MONGO_URI)

db = client["adaptive_testing"]

questions_collection = db["questions"]
sessions_collection = db["sessions"]