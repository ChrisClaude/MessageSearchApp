from pymongo import MongoClient

def get_distinct_filenames(mongodb_uri: str, database_name: str, collection_name: str) -> list[str]:
    """
    Retrieve distinct filenames from the 'metadata.source' field in the MongoDB collection.
    
    Args:
        mongodb_uri (str): MongoDB connection string.
        database_name (str): Name of the database (e.g., 'mydb').
        collection_name (str): Name of the collection (e.g., 'sermons').
    
    Returns:
        list[str]: List of unique filenames or file paths from metadata.source.
    """
    # Connect to MongoDB
    client = MongoClient(mongodb_uri)
    db = client[database_name]
    collection = db[collection_name]
    
    print("Retrieving distinct filenames from MongoDB\n\n")
    
    # Query distinct values of metadata.source
    distinct_filenames = collection.distinct("filename")
    
    # Close the connection
    client.close()
    
    print("Distinct filenames retrieved\n\n")
    
    return distinct_filenames