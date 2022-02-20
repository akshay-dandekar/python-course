# Define an empty list
myList = []


class MyClass():
    def __init__(me):
        pass

    # def __str__(self):
    #     return "this is my object at " + hex(id(self))

    def myFunction(self, someVar: int) -> str:
        print("myFunction")
        return "sadaskjdsak"


# Append integer
myTest = {"test": "val1"}
print("adding dict at " + hex(id(myTest)))
myList.append(myTest)

myTest = {"test": "val1"}
print("adding dict at " + hex(id(myTest)))
myList.append(myTest)

myList.append([])

myList.append(MyClass())

myNested = {0: {"testnested": "val1"}, "anotherkey": 23423432}


print(hex(id(myNested[0])))
myNested[0] = {"testnested": "val1"}

print(hex(id(myNested[0])))

print(myNested[0])
print(myNested[0]["testnested"])
print(myNested["anotherkey"])

# print("Using index")
# print(myList[0])

# print(myList[1])

# myList[0] = 20

# print("Using index")
# print(myList[0])

# print(myList[1])

# print("Using for")
# for element in myList:
#     element = 20
#     print(element)

#     myList[element]

# myList1 = myList

for i in range(0, len(myList)):

    # myList[i] = {}

    element = myList[i]

    print(element)
    print(hex(id(element)))

    # element = {"test":"val5"}
    # element["test"] = "val6"
