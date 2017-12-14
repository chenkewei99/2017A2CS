def binarySearch(arr,value):
    low = 0
    high = len(arr)-1
    flag = False
    while flag == False:
        mid = arr[(low+high)//2]
        if mid == value:
                flag = True
                print("it's at number ", (low+high)//2+1)
        elif value > mid:
                low = (low+high)//2-1
        elif value < mid:
                high = (low+high)//2+1


binarySearch([12,19,23,27,33,37,41,45,56,59,60,62,71,75,80,84,88,92,99],37)