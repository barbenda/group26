from pymongo import MongoClient
from pymongo.server_api import ServerApi

# MongoDB setup
uri = 'mongodb+srv://dotanber:Z91SwA0cjVUwidJw@cluster0.rte17.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
client = MongoClient(uri, server_api=ServerApi('1'))
db = client['mydatabase']  # Specify your database name

# Function to print all collections and their documents
def print_all_collections(database):
    collections = database.list_collection_names()
    for collection_name in collections:
        # fs.chunks is too big of a collection, and it deletes every collection that comes before it in the console.
        # Remove this next if statement if you want to print it
        if collection_name != 'fs.chunks':
            print(f"Collection: {collection_name}")
            collection = database[collection_name]
            documents = collection.find()
            for doc in documents:
                print(doc)
            print("\n" + "="*50 + "\n")

# Call the function
print_all_collections(db)