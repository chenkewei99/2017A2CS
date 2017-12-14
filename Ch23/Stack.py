#Kevin Chen___Stack

nullptr=-1

class Listnode (object):
    def __init__(self, value, pointer):
        self.value = value
        self.pointer = pointer

list=[0,0,0,0,0,0,0,0,0,0]
for i in range(10):
    list[i]=Listnode('','')

def Initializelist():
    global freelistptr
    global startpointer
    startpointer=nullptr
    freelistptr=0
    for i in range(0,10):
        list[i].pointer=i+1
    list[9].pointer=nullptr

def push(newvalue):
    global freelistptr
    global startpointer
    if freelistptr!=nullptr:
        newnodeptr=freelistptr
        freelistptr=list[freelistptr].pointer
        list[newnodeptr].pointer=startpointer
        startpointer=newnodeptr
        list[newnodeptr].data=newvalue

def pop():
    global freelistptr
    global startpointer
    if startpointer!=nullptr:
        currentnodeptr=startpointer
        freelistptr=currentnodeptr
        startpointer=list[currentnodeptr].pointer

def Find(v):
    global startpointer
    currentnodeptr=startpointer
    while currentnodeptr!=nullptr and list[currentnodeptr].value<=item:
        if list[currentnodeptr].data==v:
            return currentnodeptr
        else:
            currentnodeptr=list[currentnodeptr].pointer
    return nullptr

def Output():
    global startpointer
    currentptr=startpointer
    while currentptr!=nullptr:
        print(list[currentptr].data)
        currentptr=list[currentptr].pointer
