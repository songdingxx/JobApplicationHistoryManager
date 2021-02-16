from ProcessInput import *
from ConnDB import getConnection, getDatabase, getCollection, closeConnection

MONGODB_HOST = "localhost"
MONGODB_PORT = 27017
DB_NAME = "ApplicationHistory"
COLLECTION_NAME = "histories"

def main():
    conn = getConnection(MONGODB_HOST, MONGODB_PORT)
    db = getDatabase(conn, DB_NAME)
    collection = getCollection(db, COLLECTION_NAME)

    while(True):
        command = input("Please type your command\n")
        if command == "quit": 
            closeConnection(conn)
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