from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from datetime import datetime


uri = "mongodb+srv://mohamed:changeme@atlascluster.wmcjicr.mongodb.net/?retryWrites=true&w=majority&appName=AtlasCluster"
client = MongoClient(uri, server_api=ServerApi('1'))
database = client["university"]
collection = database["information"]
documents = collection.find()

def ping():
    try:
        client.admin.command('ping')
        print("Connected to MongoDB")
    except Exception as e:
        print(e)

def get_documents():
    try:
        d = []
        for document in documents:
            d.append(document)
        return d
    except Exception as e:
        print(e)

def insert(route, ip):
    try:
        document = {
            "route": route,
            "IP": ip,
            "date": datetime.now()
        }
        collection.insert_one(document)
    except Exception as e:
        print(e)

def delete():
    try:
        collection.delete_many({})
    except Exception as e:
        print(e)

if __name__ == '__main__':
    delete()