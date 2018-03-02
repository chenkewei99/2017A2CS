import pickle
from datetime import date

recordsize=50

class CarRecord :
   def __init__(self) :
    VehicleID = "dummy"
    VehicleID = VehicleID.ljust(20)
    self.VehicleID = VehicleID.encode('utf-8')
    Registration = " "
    Registration = Registration.ljust(10)
    self.Registration = Registration.encode('utf-8')
    self.DateOfRegistration = date(1990,1,1)
    self.EngineSize = 0
    self.PurchasePrice = 0.0

def inputcarrecord():
    ThisCar = CarRecord()
    VehicleID = input('Vehicle ID: ')
    VehicleID = VehicleID.ljust(20)
    ThisCar.VehicleID = VehicleID.encode('utf-8')
    Registration = input('Registration: ')
    Registration = Registration.ljust(10)
    ThisCar.Registration = Registration.encode('utf-8')
    ThisCar.DateOfregistration =(input('Registration Date: '))
    ThisCar.EngineSize = int(input('Engine size: '))
    ThisCar.PurchasePrice = float(input('Purchaseprice: '))
    return ThisCar

def Hash(reg) :
   result = ord(reg[0]) * recordsize + 1
   print('Hashed to ',result)
   return result

def SaveToFile(ThisCar, CarFile) :
    Address = Hash(ThisCar.Registration.decode('utf-8'))
    CarFile.seek(Address, 0)
    pickle.dump(ThisCar, CarFile)

def OutputData(ThisCar) :
   print(ThisCar.VehicleID)

def findrecord(reg, CarFile) :
    Address = Hash(reg)
    CarFile.seek(Address, 0)
    ThisCar = pickle.load(CarFile)
    return ThisCar

def initialize():
    global CarFile
    CarFile = open('CarFile.DAT', 'wb')
    for i in range(100):
        Address = i * recordsize + 1
        CarFile.seek(Address, 0)
        pickle.dump(CarRecord(), CarFile)
    CarFile.close()


def main():
    global CarFile
    initialize()
    inputcarrecord()
    ThisCar = CarRecord()
    ThisCar = inputcarrecord()
    SaveToFile(ThisCar, CarFile)
    ThisCar = findrecord(reg, CarFile)
    OutputData(ThisCar)
    CarFile.close()

main()
F = False
while not F :  # check for end of file
    try :
        Car.append(pickle.load(CarFile))
    except :
        F = True
