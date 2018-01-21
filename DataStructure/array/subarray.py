def maxSubArray(nums):
    """
    最大连续子序列的和  DP
    基本思路 如果前面的子序列的和>0 那么以后面一个元素为末尾的子序列一定要算上前面的子序列
    53 mmax=[]存放的是以每个元素结尾的最大子序列的和
    :type nums: List[int]
    :rtype: int
    """
    curMax,mmax=nums[0],[nums[0]]
    for i in range(1,len(nums)):
        if curMax>0:
            curMax=curMax+nums[i]
            mmax.append(curMax)
        else:
            curMax=nums[i]
            mmax.append(curMax)
    return max(mmax)

def maxSubArray_1(nums):
    """
    53  mmax存放的是最大子序列的和
    :type nums: List[int]
    :rtype: int
    """
    curMax,mmax=nums[0],nums[0]
    for i in range(1,len(nums)):
        if curMax>0:
            curMax=curMax+nums[i]
            if mmax<curMax:
                mmax=curMax
        else:
            curMax=nums[i]
            if mmax<curMax:
                mmax=curMax
    return mmax

nums=[7,-1,-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray_1(nums))

print(help(maxSubArray))