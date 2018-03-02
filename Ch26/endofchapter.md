{\rtf1\ansi\ansicpg936\cocoartf1504\cocoasubrtf830
{\fonttbl\f0\fmodern\fcharset0 Courier;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs26 \cf0 \expnd0\expndtw0\kerning0
\
### a(i)\
\pard\pardeftab720\partightenfactor0
\cf0 ```python\
	class CustomerRecord :  \
    		def \\_\\_init\\_\\_(self) :  \
			self.CustomerID = 0  \
  			self.CustomerName = ""  \
  			self.TelNumber = 0  \
  			self.TotalOrders = ""  \
```\
\
### a(ii)\
```python\
	CustomerData = \\[CustomerRecord() for i in range(10)\\]  \
```\
\
### b(i)  \
```python\
	def Hash(ID) :  \
    		return(ID % 1000) \
``` \
### b(ii)\
```python\
	def AddRecord(CustomerData, Customer):  \
    		address = Hash(Customer.CustomerID)  \
    		while CustomerData(address).CustomerID != 0 :  \
       		address += 1  \
  		if address == 1000 :  \
         		address = 0  \
  		CustomerData\\[address\\] = Customer \
``` \
\
## b(iii) \
```python\
	def FindRecord(CustomerData, ID):  \
		address = Hash(ID)  \
    		while CustomerData\\[address\\].CustomerID != ID :  \
        		address += 1  \
  		if address == 1000:  \
            	address = 0  \
  		return (address)\
```  \
  \
 ##c\
```python\
	import pickle  \
  \
	def SaveData(CustomerData) :  \
    		CustomerFile = open('CustomerData.Dat','wb')  \
    		for i in range(1000) :  \
        		pickle.dump(CustomerData\\[i\\], CustomerFile)  \
    		CustomerFile.close()\
```\
\
\
\
\
```python \
def OpenFile() :  \
    FileName = input("Which file you want? ")  \
    try:  \
        Channel = open(FileName, 'rb+')  \
    except :  \
        print("File does not exist")\
 ```}