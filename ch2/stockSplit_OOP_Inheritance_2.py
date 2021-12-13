class User():
    def __init__(self, fname, lname, age, address):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.address = address
    
    def getName(self):
        return self.fname + " " + self.lname

class StockUser():
    def __init__(self, userNumber, faceValue, nbrShares):
        self.usrNbr = userNumber
        self.faceValue = faceValue
        self.nbrShares = nbrShares

    def print_share_data(self, preText):
        totalValue = self.faceValue * self.nbrShares
        print(f"[USR{self.usrNbr}] {preText} stock split, face value: {self.faceValue} | nbr shares: {self.nbrShares} | total value: {totalValue}")

    def splitStock(self):
        self.faceValue = self.faceValue / 2
        self.nbrShares = self.nbrShares * 2

class NamedStockUser(StockUser):
    def __init__(self, userNumber, user, faceValue, nbrShares):
        super().__init__(userNumber, faceValue, nbrShares)
        self.user = user

    def print_share_data(self, preText):
        totalValue = self.faceValue * self.nbrShares
        name = self.user.getName()
        print(f"[USR{self.usrNbr}: {name}] {preText} stock split, face value: {self.faceValue} | nbr shares: {self.nbrShares} | total value: {totalValue}")

user1 = User("Akshay", "Dandekar", 29, "Sadashiv Peth")

user2 = User("Nilika", "Joshi", 24, "Upper")

usr1 = NamedStockUser(1, user2, 10, 1000)
usr1.print_share_data("Before")
usr1.splitStock()
usr1.print_share_data("After")

usr2 = StockUser(2, 5, 40)
usr2.print_share_data("Before")
usr2.splitStock()
usr2.print_share_data("After")

usr3 = StockUser(3, 7.5, 4000)
usr3.print_share_data("Before")
usr3.splitStock()
usr3.print_share_data("After")