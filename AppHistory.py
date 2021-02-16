import pymongo
from pymongo import MongoClient

MONGODB_HOST = "localhost"
MONGODB_PORT = 27017
DB_NAME = "ApplicationHistory"
COLLECTION_NAME = "histories"

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

def insertVal(collection, post):
    try:
        collection.insert_one(post)
    except:
        print("Insertion failed")

def checkParamsLength(parms, l):
    if len(parms) < l:
        print("\n(Parameters Error) Insufficient Parameters\n")
        return False
    return True

# Process input
def processInput(command, parms):
    # Insertion
    if command == "insert":
        if (checkParamsLength(parms, 3)):
            print("Insert")
        return
    # Counting
    if command == "count":
        if (checkParamsLength(parms, 2)):
            print("Count")
        return
    # Update Status by JobId
    if command == "updateStatusById":
        if (checkParamsLength(parms, 3)):
            print("updateStatusById")
        return
    # Update Status by Position
    if command == "updateStatusByPos":
        if (checkParamsLength(parms, 3)):
            print("updateStatusByPos")
        return
    # Update Status by Position
    if command == "Total":
        print("Total")
        return

def main():
    conn = getConnection(MONGODB_HOST, MONGODB_PORT)
    db = getDatabase(conn, DB_NAME)
    collection = getCollection(db, COLLECTION_NAME)

    while(True):
        command = input("Please type your command\n")
        if command == "quit": 
            conn.close()
            break
        if command == "help":
            print()
            print("Operation, [Parameters]   Seperated by comma")
            print("[insert, Company Name, JobID,Position]")
            print("[count,Parameter, Value]")
            print("[updateStatusById, Company Name, JobID, Status]")
            print("[updateStatusByPos, Company Name, Position, Status]")
            print("[Total]")
            print("[quit]")
            print()
        else:
            commands = command.split(",")
            processInput(commands[0], commands[1:])

if __name__ == "__main__":
    main()