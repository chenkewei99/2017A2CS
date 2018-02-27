#Kevin Chen Option 1

import pickle

class CarRecord :
   def __init__(self) :
        self.VehicleID = ""
        self.Registration = ""
        self.EngineSize = 0
        self.PurchasePrice = 0.0

def SaveData(Car) :
    CarFile = open('CarFile.DAT', 'wb')
    for i in range(100):
        pickle.dump(Car[i], CarFile)
        CarFile.close()

def LoadData() :
    CarFile = open('CarFile.DAT','rb')
    Car = []
    F = False
    while not F:
        try:
            Car.append(pickle.load(CarFile))
        except:
            F = True
def OutputRecords(Car) :
   for i in range(100):
       print(Car[i].VehicleID)
