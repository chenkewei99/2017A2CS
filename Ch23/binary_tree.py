

NULL = -1

class treenode:

    def __init__(self):
        self.data = " "
        self.leftptr = NULL
        self.rightptr = NULL


def initializetree():
    global rootptr
    global freeptr
    global tree

    tree = [treenode() for i in range(10)]
    rootptr = NULL
    freeptr = 0
    for i in range(10):
        tree[i].leftptr = i + 1
        tree[i].rightptr = NULL

def insert(newvalue):
    global rootptr
    global freeptr
    global tree

    if freeptr != NULL:
        newptr = freeptr
        tree[newptr].data = chr(newvalue)
        freeptr = tree[freeptr].leftptr
        tree[newptr].leftptr = NULL
        tree[newptr].rightptr = NULL

        if rootptr == NULL:
            rootptr = newptr
        else:
            tptr = rootptr
            while tptr != NULL:
                exptr = tptr
                if ord(tree[tptr].data) < newvalue:
                    Goleft = True
                    tptr = tree[tptr].leftptr
                elif ord(tree[tptr].data) > newvalue:
                    Goleft = False
                    tptr = tree[tptr].rightptr
                else:
                    print("equals value cannot be insert")
                    break

                if Goleft == True:
                    tree[exptr].leftptr = newptr
                elif Goleft == False:
                    tree[exptr].rightptr = newptr

        return(tree, rootptr, freeptr)


def find(value):
    tptr = rootptr
    while tptr != NULL and tree[tptr].data != value:
        if ord(tree[tptr].data) > value :
            tptr = tree[tptr].leftptr
        else:
            tptr = tree[tptr].rightptr
        print("the position is ", tptr)
        return(tptr)



initializetree()
insert(25)
insert(10)
insert(30)
insert(30)
find(10)
find(25)
find(30)
print(tree)