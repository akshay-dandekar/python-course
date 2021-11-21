def isValidAge(age):

    if(age < 0):
        return False
    elif(age > 120):
        return False
    else:
        return True




age = int(input("Please enter age: "))

isValid = isValidAge(age)

if(isValid):
    print("Age is valid")
else:
    print("Age is invalid")
