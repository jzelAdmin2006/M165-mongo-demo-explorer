#!/usr/bin/python3
from bson import ObjectId
from pymongo import MongoClient


def show_no_entities_message(entity):
    print("No " + entity)
    input("Press any button to return...")


def ask_user_for_database_selection():
    while True:
        db_name = input("Select a database: ")
        print(db_name)
        if db_name in dbs:
            return client[db_name]
        else:
            print("Database not found, try again...")


while True:
    connectionString = "mongodb://localhost:27017/"
    client = MongoClient(connectionString)

    dbs = client.list_database_names()
    print("Databases:")
    for db in dbs:
        print("- " + db)
    if len(dbs) == 0:
        show_no_entities_message("Database")
        continue

    db = ask_user_for_database_selection()
    collections = db.list_collection_names()
    print("Collections:")
    for collection in collections:
        print("- " + collection)
    if len(collections) == 0:
        show_no_entities_message("Collection")
        continue

    collectionName = input("Select Collection: ")
    collection = db[collectionName]
    print(db.name + "." + collectionName)

    print("Documents:")
    documents = collection.find()
    for document in documents:
        print("- " + str(document["_id"]))
    if collection.count_documents({}) == 0:
        show_no_entities_message("Document")
        continue

    documentId = input("Select Document: ")
    document = collection.find_one({"_id": ObjectId(documentId)})
    print(db.name + "." + collectionName + "." + documentId)

    for key in document:
        print(key + ": " + str(document[key]))

    input("Press any button to return...")
