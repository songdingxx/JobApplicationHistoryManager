# Helper function
# Check prams' length
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

def insertVal(collection, post):
    try:
        collection.insert_one(post)
    except:
        print("Insertion failed")