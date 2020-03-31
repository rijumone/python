from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client['tracking']

events = db['events']

print(collection.find_one())