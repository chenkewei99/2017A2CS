
# Kevin Chen option 1

class ListNode(object):
    def __init__(self ,data ,pointer):
        self.data = data;
        self.pointer = pointer;
    def __str__(self):
        return "(%s, %s)"% (self.data, self.pointer)


def InitialiseList():
    global List
    # List --> a list
    for i in range(9):
        List[i] = ListNode(None, i + 1);
    List[9] = ListNode(None, NullPointer);


def InsertNode(v):
    global StartPtr
    global List
    global FreePtr
    if FreePtr == -1:
        # FreePtr --> free pointer
        print('No room');
    if StartPtr == NullPointer:
        # StartPtr --> start pointer
        StartPtr = 0;
        FreePtr = 1;
        List[0] = ListNode(v, NullPointer);
    else:
        n = StartPtr;
        if v < List[StartPtr].data:
            F = List[FreePtr].pointer
            List[FreePtr] = ListNode(v, StartPtr);
            StartPtr = FreePtr;
            FreePtr = F;
        else:
            while True:
                if v < List[n].data:
                    m = StartPtr
                    while True:
                        if List[m].pointer == n:
                            break
                        m = List[m].pointer;
                    List[m] = ListNode(List[m].data, FreePtr);
                    List[FreePtr] = ListNode(v, n);
                    FreePtr = List[FreePtr].pointer
                    break
                elif List[n].pointer == NullPointer and v >= List[n].data:
                    F = List[FreePtr].pointer
                    List[FreePtr] = ListNode(v, NullPointer);
                    List[n] = ListNode(List[n].data, FreePtr);
                    FreePtr = F
                    break
                n = List[n].pointer;


def DeleteNode(v):
    global StartPtr
    n = StartPtr;
    while n != -1:
        if List[n].data == v:
            break
        n = List[n].pointer;
    if n == -1:
        return 'no value'
    m = FreePtr;
    while m != -1:
        if List[m].pointer == -1:
            break
        m = List[m].pointer;
    if n == StartPtr:
        StartPtr = List[n].pointer;
        List[m] = ListNode(List[m].data, n);
        List[n] = ListNode(List[n].data, NullPointer);
    elif List[n].pointer == NullPointer:
        o = StartPtr;
        while True:
            if List[o].pointer == n:
                break
            o = List[o].pointer;
        List[o] = ListNode(List[o].data, NullPointer);
        List[m] = ListNode(List[m].data, n);
    else:
        o = StartPtr;
        while True:
            if List[o].pointer == n:
                break
            o = List[o].pointer;
        List[o] = ListNode(List[o].data, List[n].pointer);
        List[m] = ListNode(List[m].data, n);
        List[n] = ListNode(List[n].data, NullPointer);


def PrintList():
    n = StartPtr;
    while n != -1:
        print(List[n].data);
        n = List[n].pointer


def SearchNode(v):
    v = int(v);
    n = StartPtr;
    while n != -1:
        if List[n].data == v:
            return n
        n = List[n].pointer;
    print('no value found');


List = [0 for i in range(10)];
NullPointer = -1;
StartPtr = NullPointer;
FreePtr = 0;
