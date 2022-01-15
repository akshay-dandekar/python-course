# Read CSV file and create appropriate objects
import stockSplit_OOP_Inheritance_2
import csv

stockUsers = []

# File parse
with open('ch2\\data.csv') as csvfile:
    dataReader = csv.DictReader(csvfile, delimiter=',')
    usrNbr = 0

    for row in dataReader:
        #print(row)
        userObj = stockSplit_OOP_Inheritance_2.User(row['Fname'], row['Lname'],
                                                    int(row['Age'], base=10),
                                                    row['Address'])
        print(userObj.getName())

        stockUser = stockSplit_OOP_Inheritance_2.NamedStockUser(
            usrNbr, userObj, int(row['FaceValue'], base=10),
            int(row['NbrStocks'], base=10))

        stockUsers.append(stockUser)

        usrNbr = usrNbr + 1

for stockUsr in stockUsers:
    stockUsr.print_share_data("Before")
    stockUsr.splitStock()
    stockUsr.print_share_data("After")
    print("-------------------------------------")