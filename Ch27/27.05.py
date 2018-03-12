import datetime
class LibraryItem:
   def __init__(self, t, a, i):
      self.__Title = t
      self.__Author_Artist = a
      self.__ItemID = i
      self.__OnLoan = False
      self.__DueDate = datetime.date.today()
      self.__BorrowerID = 0

   def Borrowing(self, b):
      self.__OnLoan = True
      self.__DueDate = self.__DueDate +datetime.timedelta(weeks=3)
      self.__BorrowerID = b

   def PrintDetails(self):
      print(self.__Title, ' ; ',self.__Author_Artist, ' ; ', end='')
      print(self.__ItemID, ' ; ', self.__OnLoan)
      print(self.__DueDate, ' ; Borrower: ',self.__BorrowerID)

class Book(LibraryItem):
    def __init__(self, t, a, i):
        LibraryItem.__init__(self, t, a, i)
        self.__IsRequested = False


    def GetIsRequested(self):
        return (self.__IsRequested)


    def SetIsRequested(self):
        self.__IsRequested = True


class CD(LibraryItem):
    def __init__(self, t, a, i):
        LibraryItem.__init__(self, t, a, i)
        self.__Genre = ""


    def GetGenre(self):
        return (self.__Genre)


    def SetGenre(self, g):
        self.__Genre = g

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
    ThisBook = Book("Sharlock Holmes", "Arthur Conan Doyle", 1028)
    ThisBook.PrintDetails()
    NewBorrower = Borrower("Kevin Chen", "ckw@gmail.com", 123)
    ThisBook.Borrowing(123)
    NewBorrower.UpdateItemsOnLoan(1)
    ThisBook.PrintDetails()
    NewBorrower.PrintDetails()