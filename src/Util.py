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