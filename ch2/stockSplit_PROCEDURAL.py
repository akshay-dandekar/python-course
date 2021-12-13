#############################################################################
#   In this example we implement the "stock split" functionality            #
#   using PROCEDURAL style                                                  #
#                                                                           #
#   In stock split, we split the share face value in half and               #
#   number of shares are doubled, so that total value of shares             #
#   remains same                                                            #
#                                                                           #
#############################################################################


# For user 1
usr1FaceValue = 10
usr1NbrShares = 1000
usr1TotalVal = usr1FaceValue * usr1NbrShares

print(f"[USR1] Before stock split, face value: {usr1FaceValue} | nbr shares: {usr1NbrShares} | total value: {usr1TotalVal}")

# Perform "stock split" operation
usr1FaceValue = usr1FaceValue / 2
usr1NbrShares = usr1NbrShares * 2
usr1TotalVal = usr1FaceValue * usr1NbrShares

print(f"[USR1] After stock split, face value: {usr1FaceValue} | nbr shares: {usr1NbrShares} | total value: {usr1TotalVal}")

print("-------------------------------------")


# For user 2
usr2FaceValue = 5
usr2NbrShares = 350
usr2TotalVal = usr2FaceValue * usr2NbrShares

print(f"[USR2] Before stock split, face value: {usr2FaceValue} | nbr shares: {usr2NbrShares} | total value: {usr2TotalVal}")

# Perform "stock split" operation
usr2FaceValue = usr2FaceValue / 2
usr2NbrShares = usr2NbrShares * 2
usr2TotalVal = usr2FaceValue * usr2NbrShares

print(f"[USR2] After stock split, face value: {usr2FaceValue} | nbr shares: {usr2NbrShares} | total value: {usr2TotalVal}")

print("-------------------------------------")


# If want to add program for another user, Need to copy paste all above lines once more
# Also need to change the variable names for "face value", "number of shares" and 
# "total value"
#
# This becomes tedeous, prone to errors and repetitive task
#
# Also if there is small change in the requirement, 
# e.g. Print should have user name also in the bracket like [USR1: Akshay] 
# 
# This style will make the code change very hard and time cosuming task.
# Hence we will shift to FUNCTIONAL style programming
#