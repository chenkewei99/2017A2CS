{\rtf1\ansi\ansicpg936\cocoartf1504\cocoasubrtf830
{\fonttbl\f0\fmodern\fcharset0 Courier;\f1\fnil\fcharset134 PingFangSC-Regular;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs26 \cf0 \expnd0\expndtw0\kerning0
# task 1\
1.1\
JSP diagrams can show the structure of the program, including all the functions and parameters.\
It can also indicate the iterations and chooses to be made\
\
1.2\
the * means to iterate the operationall\
the 
\f1 \'a1\'a3
\f0 meand to select between two situations\
\
1.3\
\
NOT EOF\
salary>50\
slalary>=90\
projectmanager\
leaddeveloper\
manager\
\
1.4\
\
Add another block that says salary>70
\f1 \'a1\'a3
\f0 \
if Flase, assign the role as leaddeveloper\
if True, goes to the selection of salary>=90\
change that False situation to assign the role as consultant\
\
1.5\
\
Change line 5 to IF salary>=70\
Change line 6 to IF salary>=90\
Change rest of the program to be like:\
            THEN Role<---projectmanager\
            ElSE Role<---consultant\
        ENDIF\
    ELSE\
        Role<---leaddeveloper\
ELSE\
    Role<---manager\
    \
    \
1.6\
\
    def determinerole(salary):\
        if salary>50:\
            if salary>70:\
                if salary>=90\
                    return 'projectmanager'\
                else:\
                    return 'consultant'\
            else:\
                return 'leaddeveloper'\
        else:\
            return 'manager'\
\
\
\
\pard\pardeftab720\partightenfactor0
\cf0 # task 2\
\
2.1\
TOY:\
Attributes        | Functions\
Name              | getname( )/setname( )\
ID                    | getID( )/setID( )\
Price               | getPrice( )/setPrice( )\
Minimum age  | getMinimumage( )/setMinimumage( )\
\
ComputerGame:\
Attributes        | Functions\
Category         | getcategory( )/setcategory( )\
Console          | getconsole( )/setconsole( )\
\
Vehicle\
Attributes        | Functions\
Type                | gettype( )/settype( )\
Height             | getheight( )/setheight( )\
Length             | getlength( )/setlength( )\
Weight             | getweight( )/setweight( )\
\
2.2\
inheritence means that one class's parameters is directly passed down to its subclasses\
\
In the last example, computergame and vehicle are the subclasses of toy.\
\
2..3\
\
    class toy:\
        def __init__(self,n,i,p,m):\
            self.__name=n\
            self.__id=i\
            self.__price=p\
            self.__minimumage=m\
        \
        def getname(self):\
            return self.__name\
            \
        def setname(self,name):\
            self.__name=name\
            \
        def getid(self):\
            return self.__id\
        \
        def setid(self,id):\
            self.__id=id\
        \
        def getprice(self):\
            return self.__price\
            \
        def setprice(self):\
            self.__price=price\
        \
        def getminimumage(self):\
            return self.__minimumage\
       \
       def setminimumage(self,min):\
            self.m__minimumage=mim\
            \
        \
2.4\
\
    class vehicle(toy):\
        def__init__(self,n,i,p,m,t,h,l,w):\
            toy.__init__(self,n,i,p,m):\
            self.__type=t\
            self.__height=h\
            self.__weight=w\
            self.__length=l\
            \
            \
2.5\
\
    try:\
        if age>0 and age<18:\
            self.age=age\
        else:\
            age=input('please input again')\
        \
\
2.6\
\
    vehicle=[ ]\
    computergame=[ ]\
    vehicle.append('red sports car','RSC13',15.00,6,'car',3.3,12.1,0.08)\
    \
2.7\
\
    def printdetails(id):\
       i=0\
       while toy[i].id!=id:\
            i+=1\
       Toy[i].printdetails()\
        \
        \
2.8\
\
    def discount(n):\
        n=n/100\
        for i in range(len(toy)):\
            toy[i].prince=toy[i].price*n\
    \
\
2.9\
\
 a bubble sort changes the order of the list one item and another by comparing the two near once at a time.\
 a insertion sort does it by finding the approperiate position to insert the item\
 \
 2.10\
 \
 \
    def sort():\
        for i in range(1,len(toys)):\
            itemtobeinserted=toy[i]\
            c=i-1\
            while itemtobeinserted.price<toy[c].price and c>0:\
                toy[c+1]=toy[c]\
                c-=1\
            toy[c+1]=itemtobeinserted\
\
\
\
\
\
\
\
\pard\pardeftab720\partightenfactor0
\cf0 \
\
\
\
\
\
\
\
}