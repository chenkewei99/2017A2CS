#CodingBat Recursion1
#Kevin Chen
#Option 1


def factorial(n):
    if n==1:
        return 1
    return n*(factorial(n-1))

#print(factorial(4))

def bunnyEars(bunnies):
    if bunnies==0:
        return 0
    return 2+bunnyEars(bunnies-1)

#print(bunnyEars(4))

def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)

#print(fibonacci(5))

def bunnyEars2(bunnies):
    if bunnies==0:
        return 0
    elif bunnies%2==1:
        return 2+bunnyEars2(bunnies-1)
    return 3+bunnyEars2(bunnies-1)

#print(bunnyEars2(3))

def triangle(rows):
    if rows==0:
        return 0
    if rows==1:
        return 1
    return rows+triangle(rows-1)

#print(triangle(3))

def sumDigits(n):
    if n==0:
        return 0
    return n%10+sumDigits(n//10)

#print(sumDigits(1245))

def count7(n):
    if n==0:
        return 0
    if n%10==7:
        return 1+count7(n//10)
    return count7(n//10)

#print(count7(17177))

def count8(n):
    if n==8:
        return 1
    if n%100==88:
        return 2+count8(n//10)
    if n%10==8:
        return 1+count8(n//10)

    return count8(n//10)

#print(count8(8188298))

def powerN(base,n):
    if n==1:
        return base
    n = n - 1
    return base*powerN(base,n)

#print(powerN(4,3))

def countX(str):
    if len(str)==1 and str[0] == 'x':
        return 1
    elif str[0] == "x":
        return 1 + countX(str[1:])
    elif str[0] !="x":
        return countX(str[1:])

#print(countX("xxq2exrxx"))


def countHi(str):
    if len(str)==2 and str[0:2] == 'hi':
        return 1
    elif str[0:2] == "hi":
        return 1 + countHi(str[1:])
    elif str[0:2] !="hi":
        return countHi(str[1:])

#print(countHi("ahisbjhishi"))

def changeXY(str):
    if len(str)==1 and str=='x':
        return 'y'
    if str[0]== 'x':
        return 'y'+changeXY(str[1:])
    else:
        return str[0]+changeXY(str[1:])

#print(changeXY("xfgxhx"))

def changePi(str):
    if len(str)==2 and str=='pi':
        return '3.14'
    if str[0:2]== 'pi':
        return '3.14'+changePi(str[2:])
    else:
        return str[0]+changePi(str[1:])

#print(changePi("xpifghjgpi"))

def noX(str):
    if len(str)==1 and str=='x':
        return ''
    if str[0]=='x':
        return '' + noX(str[1:])
    else:
        return str[0]+noX(str[1:])

#print(noX('xfxxxxxxghxcx'))

def array6(nums, index):
    if index == len(nums)-1 and nums[index] != 6:
        return False
    if nums[index]==6:
        return True

    else:
        index += 1
        return array6(nums, index)

#print(array6([1,4,8,76,6], 0))

def array11(nums, index):
    if index == len(nums)-1 and nums[index]==11:
        return 1
    if index == len(nums)-1 and nums[index]!=11:
        return 0
    if nums[index] == 11:
        return 1 + array11(nums,index+1)
    else:
        return array11(nums, index+1)

#print(array11([11,3,11,4,11],0))

def array220(nums, index):
    if len(nums)==1:
        return False
    if len(nums)==2 and (nums[index]*10) != nums[index+1]:
        return False
    if ((nums[index]*10)==nums[index+1]) and (index+1<len(nums)):
        return True

    else:
        return array220(nums, index+1)

#print(array220([2,3,6,5,77,770,2,4,2],0))

def allStar(str):
    if str=='':
        return ''
    if len(str)>1:
        return str[0]+'*'+allStar(str[1:])
    else:
        return str[0]

#print(allStar('hello'))

def pairStar(str):
    if str=='':
        return ''
    if len(str)>1 and str[0]==str[1]:
        return str[0]+'*'+pairStar(str[1:])
    else:
        return str[0]+pairStar(str[1:])

#print(pairStar('xx12ss34yy56hello'))

def endX(str):
    if str=='':
        return ''
    if str[0]=='x':
        return endX(str[1:])+'x'
    else:
        return str[0]+endX(str[1:])

#print(endX('xhixhixhi'))

def countPairs(str):
    if str=='':
        return 0
    if len(str)>=3 and str[0]==str[2]:
        return 1+countPairs(str[1:])
    else:
        return countPairs(str[1:])

#print(countPairs("axaxbxb"))

def countAbc(str):
    if str=='':
        return 0
    if len(str)>=3 and str[0:3]=='abc':
        return 1+countAbc(str[3:])
    if len(str)>=3 and str[0:3]=='aba':
        return 1+countAbc(str[1:])
    else:
        return countAbc(str[1:])

#print(countAbc("abcxababa"))

def count11(str):
    if str=='':
        return 0
    if len(str)>=2 and str[0:2]=='11':
        return 1+count11(str[2:])
    else:
        return count11(str[1:])

#print(count11('11abc111x11x11'))

def stringClean(str):
    if str=='':
        return ''
    if len(str)>=2 and str[0]==str[1]:
        return stringClean(str[1:])
    else:
        return str[0]+stringClean(str[1:])

#print(stringClean('aabbbccccddddd'))

def countHi2(str):
    if str=='':
        return 0
    if len(str)>=3 and str[0:3]=='xhi':
        return 0+countHi2(str[3:])

    if len(str)>=2 and str[0:2]=='hi':
        return 1+countHi2(str[1:])
    else:
        return 0+countHi2(str[1:])

#print(countHi2('hixhixhixhiahibhichi'))

def parenBit(str):
    if str=='':
        return ''
    if str[0]!='(':
        return parenBit(str[1:])
    if str[-1]!=')':
        return parenBit(str[:-1])
    else:
        return str

#print(parenBit('xyz(abc)123'))

def nestParen(str):
    if str=='':
        return True
    if str[0]=='(' and str[-1]==')':
        return nestParen(str[1:-1])
    else:
        return False

#print(nestParen('(((x)))'))

def strCount(str, sub):
    if str=='':
        return 0
    if str[0:len(sub)]==sub:
        return 1+strCount(str[len(sub):], sub)
    else:
        return strCount(str[1:], sub)

#print(strCount("dogacatadoga", 'doga'))]

def strCopies(str, sub, n):

    if str=='' and n==0:
        return True
    if str=='' and n!=0:
        return False
    if str[0:len(sub)]==sub:
        n -= 1
        return strCopies(str[len(sub):], sub, n)
    else:
        return strCopies(str[1:], sub, n)

#print(strCopies("dogacatadoga", 'doga', 2))

def strDist(str, sub):
    if str[0:len(sub)] != sub:
        return strDist(str[1:], sub)
    if str[-len(sub):] != sub:
        return strDist(str[:-1], sub)
    else:
        return len(str)

#print(strDist("aaaaacatcowcataaaaaa", 'cat'))