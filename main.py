#!/usr/bin/python3
from bson import ObjectId
from bson.errors import InvalidId
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


def ask_user_for_collection_selection():
    while True:
        collection_name = input("Select a collection: ")
        print(db.name + "." + collection_name)
        if collection_name in collections:
            return db[collection_name]
        else:
            print("Collection not found, try again...")


def ask_user_for_document_selection():
    while True:
        document_id = input("Select a document: ")
        print(db.name + "." + collection.name + "." + document_id)
        try:
            if collection.count_documents({"_id": ObjectId(document_id)}) > 0:
                return collection.find_one({"_id": ObjectId(document_id)})
            else:
                print("Document not found, try again...")
        except InvalidId:
            print("This is an invalid ID, try again...")


connectionString = "mongodb://localhost:27017/"
client = MongoClient(connectionString)
dbs = client.list_database_names()
while True:
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

    collection = ask_user_for_collection_selection()
    print("Documents:")
    documents = collection.find()
    for document in documents:
        print("- " + str(document["_id"]))
    if collection.count_documents({}) == 0:
        show_no_entities_message("Document")
        continue

    document = ask_user_for_document_selection()
    for key in document:
        print(key + ": " + str(document[key]))

    input("Press any button to return...")
