import pymongo
from pymongo import MongoClient


# Try to build connection
def getConnection(host, port):
    try:
        connection = MongoClient(host, port)
        return connection
    except:
        print("Get connection failed")
        exit()

# Try to get database
def getDatabase(connection, dbName):
    try:
        database = connection[dbName]
        return database
    except:
        print("Get database failed")
        exit()

# Try to find collection
def getCollection(database, colName):
    try:
        collection = database[colName]
        return collection
    except:
        print("Get collection Failed")
        exit()

# Close connection
def closeConnection(conn):
    try:
        conn.close()
    except:
        print("Failed to close the connection")
        exit()