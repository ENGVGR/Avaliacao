listOfStrings = []

def stringConvert(entry):
    entry = list(entry)
    while len(entry) > 0:
        listOfStrings.append(entry.pop())

def listToString(entry):
    newString = ""
    while len(entry) > 0:
        newString += entry.pop(0)
    return newString

entry = input()
stringConvert(entry)

print(listToString(listOfStrings))