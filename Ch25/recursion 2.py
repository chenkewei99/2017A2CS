#Solutions for CodingBat Recursion2
#Kevin Chen
#Option 1

def groupSum(start, nums, target):
    if target == 0:
        return True

    if start == len(nums):
        return False

    return groupSum(start+1, nums, target - nums[start]) or groupSum(start+1, nums, target)

#print(groupSum(0, [2,2,4,3,5], 9))

def groupSum6(start, nums, target):
    if start == len(nums):
        return target==0

    if nums[start]==6:
        return groupSum6(start+1, nums, target-nums[start])
    elif target==0 and start != len(nums):
        return groupSum6(start+1, nums, target)

    return groupSum6(start+1, nums, target - nums[start]) or groupSum(start+1, nums, target)

#print(groupSum6(0, [5, 6, 3, 2], 7))

def groupNoAdj(start, nums, target):

    if target == 0:
        return True

    if start >= len(nums):
        return False

    return groupNoAdj(start+2, nums, target-nums[start]) or groupNoAdj(start+1, nums, target)

#print(groupNoAdj(0, [2, 20, 20, 5, 10, 4], 7))

def groupSum5(start, nums, target):
    if start == len(nums):
        return target == 0

    if nums[start]%5==0 and nums[start+1]==1:
        return groupSum5(start+2, nums, target)

    if nums[start]%5==0:
        return groupSum5(start+1, nums, target-nums[start])

    return groupSum5(start+1, nums, target) or groupSum5(start+1, nums, target-nums[start])

#print(groupSum5(0, [2, 5, 10, 4], 14))

def groupSumClump(start, nums ,target):
    if target == 0:
        return True

    if start == len(nums):
        return False

    if start < len(nums)-1 and nums[start]==nums[start+1]:
        n=0
        for i in range(len(nums)-2):
            if nums[start]==nums[start+i+1]:
                    n += 1

        return groupSumClump(start+n, nums, target-n*nums[start]) or groupSumClump(start + n, nums, target)


    return groupSumClump(start+1, nums ,target - nums[start]) or groupSumClump(start+1, nums, target)

#print(groupSumClump(0, [2, 3, 3, 3,3,3,3,3,3,3,3,3], 2))

def helperForSplitArray(start, nums, sum1, sum2):
    if start >= len(nums) and sum1==sum2:
        return True
    if start >= len(nums):
        return False
    return helperForSplitArray(start+1, nums, sum1+nums[start], sum2) \
           or helperForSplitArray(start+1, nums, sum1, sum2+nums[start])

def splitArray(nums):
    if helperForSplitArray(0, nums, 0, 0) == True:
        return True
    else:
        return False

#print(splitArray([5,4,1,3]))

def helperForSplitOdd10(start, nums, sum1, sum2):
    if sum1 != 0 and sum2%2==1 and sum1%10 == 0 :
        return True

    if start >= len(nums):
        return False
    return helperForSplitOdd10(start+1, nums, sum1+nums[start], sum2) or helperForSplitOdd10(start+1, nums, sum1, sum2+nums[start])

def splitOdd10(nums):
    if helperForSplitOdd10(0, nums, 0, 0)==1:
        return True
    else:
        return False

#print(splitOdd10([5,5,6,1]))

def helper53(start, sum, sum5, sum3):
    if start>=len(sum):
        return(sum5==sum3)
    if sum[start]%5==0:
        return helper53(start + 1, sum, sum5 + sum[start], sum3)
    if sum[start]%3==0:
        return helper53(start + 1, sum, sum5, sum3 + sum[start])
    return helper53(start + 1, sum, sum5 + sum[start], sum3) or helper53(start + 1, sum, sum5, sum3 + sum[start])

def split53(sum):
    return helper53(0, sum, 0, 0)

#print(split53([3,5,3,3,3,3,5,5]))