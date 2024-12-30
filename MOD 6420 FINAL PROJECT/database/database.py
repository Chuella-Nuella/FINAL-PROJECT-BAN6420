from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from urllib.parse import quote_plus
import logging

logging.basicConfig(level=logging.DEBUG)

# Encode username and password
username = quote_plus("Nuella")
password = quote_plus("db_Angel@Ojone123")
database_name = "SurveyDB"  

# Connection URI with authSource and retry settings
uri = f"mongodb+srv://{username}:{password}@surveymanagement.bemkb.mongodb.net/{database_name}?retryWrites=true&w=majority&appName=SurveyManagement&authSource=admin"

client = MongoClient(uri, server_api=ServerApi('1'))

# Access the SurveyDB database
db = client[database_name]  # Corrected to use SurveyDB

# Access the 'User Information' collection
user_collection = db["User Information"]

try:
    client.admin.command('ping')
    print("Successfully connected to MongoDB!")
except Exception as e:
    print(f"Failed to connect: {e}")