#############################################################################
#   In this example we implement the "stock split" functionality            #
#   using FUNCTIONAL style                                                  #
#                                                                           #
#   In stock split, we split the share face value in half and               #
#   number of shares are doubled, so that total value of shares             #
#   remains same                                                            #
#                                                                           #
#############################################################################

# 
# In case of functional, we find the common functionality/repetitive task
# Then we club it into a function, which will be "called" multiple times
# every time with new set of data
#
# A function can have no arguments (no inputs), it will perform common steps
# on input data, and may or may not return the results
# e.g. a print only function will not return anything, but the stockSplit
# function will return new values for "face value" and "number of shares"
#


#
# In case of sock split funtionality, we found that there are two common 
# tasks are 
# - to print the stock data 
# - To split the sock and calculate new values for "face value" 
#   and "nbr shares"
#
# We then creates these two functions and called them with diffrerent 
# arguments (input data) for each user
# 
# This made the code easy to maintain and less prone to error
# 
# Also when client asked for a small change of adding the user name
# We created another function for print data, and called that function
# whenever required.
#


# Function to print stock data (with user name)
def print_share_data(usrNbr, preText, faceValue, nbrShares):
    totalValue = faceValue * nbrShares
    print(
        f"[USR{usrNbr}] {preText} stock split, face value: {faceValue} | nbr shares: {nbrShares} | total value: {totalValue}"
    )


# Function to print stock data (with user name)
def print_share_data_with_name(usrNbr, usrName, preText, faceValue, nbrShares):
    totalValue = faceValue * nbrShares
    print(
        f"[USR{usrNbr}, {usrName}] {preText} stock split, face value: {faceValue} | nbr shares: {nbrShares} | total value: {totalValue}"
    )


# Function to perform stock split operation
def splitStock(initalFaceValue, currentNbrShares):
    newFaceValue = initalFaceValue / 2
    newNbrShares = currentNbrShares * 2

    return (newFaceValue, newNbrShares)


# For user 1
usr1FaceValue = 10
usr1NbrShares = 1000

retValu = print_share_data(1, "Before", usr1FaceValue, usr1NbrShares)

usr1FaceValue, usr1NbrShares = splitStock(usr1FaceValue, usr1NbrShares)

print_share_data(1, "After", usr1FaceValue, usr1NbrShares)

print("-------------------------------------")

# For user 2
usr2FaceValue = 4
usr2NbrShares = 2400

retValu = print_share_data(2, "Before", usr2FaceValue, usr2NbrShares)

usr2FaceValue, usr2NbrShares = splitStock(usr2FaceValue, usr2NbrShares)

print_share_data(2, "After", usr2FaceValue, usr2NbrShares)

print("-------------------------------------")

# For user 3
usr3FaceValue = 6
usr3NbrShares = 780

retValu = print_share_data_with_name(3, "Akshay", "Before", usr3FaceValue, usr3NbrShares)

usr3FaceValue, usr3NbrShares = splitStock(usr3FaceValue, usr3NbrShares)

print_share_data_with_name(3, "Akshay", "After", usr3FaceValue, usr3NbrShares)

print("-------------------------------------")
