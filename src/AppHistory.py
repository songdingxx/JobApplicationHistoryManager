from ProcessInput import processInput
from Util import processString, processStringArray
from ConnDB import getConnection, getDatabase, getCollection, closeConnection

MONGODB_HOST = "localhost"
MONGODB_PORT = 27017
DB_NAME = "ApplicationHistory"
COLLECTION_NAME = "histories"
VALID_OPERATION = {"insert", "count", "updatestatus", "findjobs", "total"}

def main():
    conn = getConnection(MONGODB_HOST, MONGODB_PORT)
    db = getDatabase(conn, DB_NAME)
    collection = getCollection(db, COLLECTION_NAME)
    while(True):
        command = input("Please type your command - Type \"help\" for help\n")
        if command == "quit": 
            closeConnection(conn)
            break
        if command == "help":
            print()
            print("Operation, [Parameters]   Seperated by comma")
            print("[insert, Company Name, JobID,Position]")
            print("[count,Parameter, Value]")
            print("[updateStatus, Company Name, param, Status, Option (default = 0) (0: param = JobID， 1：param = Position)]")
            print("[findJobs, Company Name, param, Option (default = 0) (0: param = JobID， 1：param = Position)]")
            print("[total]")
            print("[quit]")
            print()
        else:
            commands = command.split(",")
            try:
                c_ = processString(commands[0])
                params = processStringArray(commands[1:])
            except Exception as e:
                print(e.args)
            
            if c_ not in VALID_OPERATION:
                print("\nInvalid operation!\n")
                continue

            processInput(c_, params, collection)

if __name__ == "__main__":
    main()