
### a(i)

```Python
    class CustomerRecord :
        def \_\_init\_\_(self) :
            self.CustomerID = 0
            self.CustomerName = ""
            self.TelNumber = 0
            self.TotalOrders = ""
```
### a(ii)
```Python
    CustomerData = \[CustomerRecord() for i in range(10)\]
```
### b(i)

```Python
    def Hash(ID) :
        return(ID % 1000)
```

### b(ii)
```Python
    def AddRecord(CustomerData, Customer):
        address = Hash(Customer.CustomerID)
        while CustomerData(address).CustomerID != 0 :
            address += 1
            if address == 1000 :
            address = 0
            CustomerData\[address\] = Customer
```
### b(iii)
```Python
    def FindRecord(CustomerData, ID):
        address = Hash(ID)
        while CustomerData\[address\].CustomerID != ID :
            address += 1
            if address == 1000:
                address = 0
                return (address)
```

### c

```Python
    import pickle

    def SaveData(CustomerData) :
        CustomerFile = open('CustomerData.Dat','wb')
        for i in range(1000) :
            pickle.dump(CustomerData\[i\], CustomerFile)
        CustomerFile.close()
```




```python

    def OpenFile() :
        FileName = input("Which file you want? ")
        try:
            Channel = open(FileName, 'rb+')
        except :
            print("File does not exist")
```
