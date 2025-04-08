from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os

from dotenv import load_dotenv
load_dotenv()


def get_mongo_client():
    try:
        # Set the MongoDB connection string
        mongo_uri = os.environ["DB_URL"]

        # Create a MongoClient to the running mongod instance
        client = MongoClient(mongo_uri, server_api=ServerApi('1'))

        return client
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")
        return None
