def solve(idx,nums):
    '''
    idx
    :param idx:
    :param nums:
    :return:
    '''
    if idx<0:
        return 0
    if idx==0:
        return nums[0]
    if idx==1:
        return nums[1]
    return min(nums[idx]+solve(idx-2,nums),nums[idx-1]+solve())

print(solve(4,[1,5,1,1,5]),solve(3,[1,5,1,1,5]))