class Borrower():
    def __init__(self, n, e, b):
        self.__BorrowerName = n
        self.__EmailAddress = e
        self.__BorrowerID = b
        self.__ItemsOnLoan = 0

    def GetBorrowerName(self):
        return (self.__BorrowerName)

    def GetEmailAddress(self):
        return (self.__EmailAddress)

    def GetBorrowerID(self):
        return (self.__BorrowerID)

    def GetItemsOnLoan(self):
        return (self.__ItemsOnLoan)

    def UpdateItemsOnLoan(self, n):
        self.__ItemsOnLoan += n

    def PrintDetails(self):
        print("Borrower:", self.__BorrowerName)
        print("ID:", self.__BorrowerID)
        print("email:", self.__EmailAddress)
        print("Items on loan: ", self.__ItemsOnLoan)

def main():
    NewBorrower = Borrower("Kevin Chen", "ckw@gmail.com", 123)
    NewBorrower.UpdateItemsOnLoan(3)
    NewBorrower.PrintDetails()
    NewBorrower.UpdateItemsOnLoan(-1)
    NewBorrower.PrintDetails()

