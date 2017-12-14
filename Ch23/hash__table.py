table = [0]*10

def insert(newrecord):
    i = newrecord % 10
    while table[i] != 0:
        i = i + 1
        if i > 9:
            i = 1

    table[i] = newrecord

def find(searchvalue):
    i = searchvalue % 10
    while table[i] != searchvalue and table[i] != 0:
        i = i + 1
        if i > 9:
            i = 0
    if table[i] != 0:
        print(i)
        return i

insert(23)
insert(35)
find(35)
find(23)


