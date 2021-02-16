from datetime import datetime

# Helper function
# Check prams' length
def checkParamsLength(params, l):
    if len(params) < l:
        print("\n(Parameters Error) Insufficient Parameters\n")
        return False
    return True

# Process String - remove spaces at begining and end, convert to lower case
def processString(s):
    try:       
        return s.strip().lower()
    except:
        raise Exception("Process string error")

# Process the array of strings
def processStringArray(ss):
    try:
        ss_ = []
        for s in ss: ss_.append(processString(s))
        return ss_
    except:
        raise Exception("Process string array error")

# Process empty string
def processEmptyString(s):
    return s if s != "" else "None"

# Get now in string format
def getNowString():
    now = datetime.now()
    return now.strftime("%d/%m/%Y %H:%M:%S")

# Print record in a pretty way
def printPretty(record):
    if not isinstance(record, dict): return
    print("{")
    for i, v in record.items():
        print("%20s: %20s" %(i, v))
    print("}\n")

# Process input
def processInput(command, params, collection):
    # Insertion
    if command == "insert":
        if (checkParamsLength(params, 3)):
            insertToDB(collection, params)
        return
    # Counting
    if command == "count":
        if (checkParamsLength(params, 2)):
            countByParam(collection, params)
        return
    # Update Status
    if command == "updatestatus":
        if (checkParamsLength(params, 3)):
            updateStatus(collection, params)
        return
    # Find jobs
    if command == "findjobs":
        if (checkParamsLength(params, 2)):
            findJobs(collection, params)
        return
    # Update Status by Position
    if command == "total":
        totalApplications(collection)
        return

# DB operations
# Insertion - insert if there isn't an indetical application
# TODO: Potential Problem: Companies could have same names, add instudry info?
# TODO: There is a Bug here, if I implemented the deletion, Indices can be duplicated
# Can be solved by giving random index, am I going to use the index？
# TODO: colleciton.count() takes O(n) time, is there a way to get last inserted index in O(1) time?
def insertToDB(collection, params):
    index = collection.count()

    if processEmptyString(params[0]) == "None":
        print("\n(Insertion Error) Must type in a company name\n")
        return
    
    res = collection.find({
            "company name": processEmptyString(params[0]), 
            "jobID": processEmptyString(params[1]),
            "position": processEmptyString(params[2])})

    if res.count() != 0:
        print("\n(Insertion Error) There is an identical record already\n")
        printPretty(res[0])
        return

    post = {"_id": index, 
            "company name": processEmptyString(params[0]), 
            "jobID": processEmptyString(params[1]),
            "position": processEmptyString(params[2]),
            "timestamp": getNowString(),
            "status": "pending"}
    try:
        collection.insert_one(post)
        print("\nInsertion succeed\n")
    except:
        print("\n(Insertion error) Database problem, with a great chance to be the index problem\n")

# Update status by position or jobID
# Default option is jobID
def updateStatus(collection, params):
    option = "jobID" if len(params) < 4 or params[3] == "0" else "position"
    try:
        collection.update_one(
            {"company name": params[0], option: params[1]},
            {"$set": {"status": params[2]}})
        print("\nStatus has been updated to %s.\n" %(params[2]))
    except:
        print("\n(Update error) Database error.\n")

# Find job by position or jobID
# Default option is jobID
def findJobs(collection, params):
    option = "jobID" if len(params) < 3 or params[2] == "0" else "position"
    try:
        res = collection.find({"company name": params[0], option: params[1]})
        if res.count() == 0:
            
            print("\nThere is no such job, please check the input\n")
            return
        print("\nFound %d records\n" %(res.count()))
        for x in res:
            printPretty(x)
    except:
        print("\n(Find error) Database error.\n")

# Count records by param == val
# TODO: Doesn't suppot <, > yet
def countByParam(collection, params):
    res = collection.find({params[0]:params[1]})
    print("\nThere are %d jobs relate to it." %(res.count()))
    for x in res:
        printPretty(x)
    print()

# Count the number of applications
def totalApplications(collection):
    print("\nApplied for %d jobs already. You got this boss!\n" %(collection.count()))