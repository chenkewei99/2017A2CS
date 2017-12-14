def bubblesort(array):
    if array:
        flag = False
        length = len(array)
        while not flag:
            flag = True
            for i in range(length):
                if array[i]>array[i+1]:
                    number = array[i+1]
                    array[i+1] = array[i]
                    array[i] = number
                    flag = False     
    return array
