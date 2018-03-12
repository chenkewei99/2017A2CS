import datetime
class LibraryItem:
    def __init__(self, t, a, i):
        self.__Title = t
        self.__Author_Artist = a
        self.__ItemID = i
        self.__OnLoan = False
        self.__DueDate = datetime.date.today()

    def GetTitle(self):
       return(self.__Title)

    def GetAuthor_Artist(self):
       return(self.__Author_Artist)

    def GetItemID(self):
        return (self.__ItemID)

    def GetOnLoan(self):
        return (self.__OnLoan)

    def GetDueDate(self):
        return (self.__DueDate)

    def Borrowing(self):
        self.__OnLoan = True
        self.__DueDate = self.__DueDate +datetime.timedelta(weeks=3)

    def Returning(self):
        self.__OnLoan = False

    def PrintDetails(self):
        print(self.__Title, ' ; ', self.__Author_Artist,end='')
        print(' ; ', self.__ItemID, ' ; ', self.__OnLoan,end='')
        print(' ; ', self.__DueDate)

class Book(LibraryItem):
    def __init__(self, t, a, i):
        LibraryItem.__init__(self, t, a, i)
        self.__IsRequested = False
        self.__RequestedBy = 0


    def GetIsRequested(self):
        return (self.__IsRequested)


    def SetIsRequested(self, b):
        self.__IsRequested = True
        self.__RequestedBy = b

def PrintDetailsOfBook(self):
    print("Book Details")
    LibraryItem.PrintDetails(self)
    if self.__IsRequested:
        print('Requested by ', self.__RequestedBy)
    else:
        print('no requests')



class CD(LibraryItem):
    def __init__(self, t, a, i):
        LibraryItem.__init__(self, t, a, i)
        self.__Genre = ""


    def GetGenre(self):
        return (self.__Genre)


    def SetGenre(self, g):
        self.__Genre = g


def PrintDetailsOfCD(self):
   print("CD Details")
   LibraryItem.PrintDetails(self)
   print(self.__Genre)