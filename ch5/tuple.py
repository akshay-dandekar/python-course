def getValsList():
    myList = []
    myList.append({"key1":"val1"})
    myList.append(9385)
    myList.append("983453894753894")
    return myList


def getValsTuple():
    return ({"key1":"val1"}, 9385, "983453894753894")

my1st, ret, ret1  = getValsTuple()

print(my1st)

myRet1 = getValsList()
print(myRet1)


