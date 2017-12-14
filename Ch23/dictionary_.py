#dictionary from Kevin Chen Option 1

NULL = -1

class dictionary:

    def __init__(self):
        self.word = " "
        self.defi = " "

dictionary = [dictionary() for i in range(20)]
for i in range(20):
    dictionary[i].word = NULL
    dictionary[i].defi = NULL

def insert(W, D):
    i = ord(W[0]) % 10
    while dictionary[i].word != NULL:
        i = i + 1
        if i > 19:
            i = 1

    dictionary[i].word = W
    dictionary[i].defi = D



def find(searchvalue):
    i = ord(searchvalue[0]) % 10
    while dictionary[i].word != searchvalue and dictionary[i].word != NULL:
        i = i + 1
        if i > 19:
            i = 0
    if dictionary[i].defi != NULL:
        print("the definition of ", dictionary[i].word, "is ",dictionary[i].defi)
        return dictionary[i].defi


insert("Abstract data type", "a collection of data with associated operations")
insert("Binary search", "repeated checking of the middle item in an ordered search list and discarding the half ofthe list whichdoes not containthesearchitem")
insert("Sensor", "a hardware device that measures a property and transmits a value to a controlling computer")
insert("Plaintext", "data before encryption")
insert("Actuator", "a hardware device that receives a signal from a computer and adjusts the setting of a controlling device")
find("Binary search")
find("Abstract data type")
find("Actuator")

insert("a", 'asda')
insert("a", "fdasd")
find("a")