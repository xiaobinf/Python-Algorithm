class Solution:
    def canJump(self, nums):
        """
        leetcode 55
        :type nums: List[int]
        :rtype: bool
        """
        i=0
        lastPos=len(nums)-1
        for i in reversed(range(len(nums))):
            if i+nums[i]>=lastPos:
                lastPos=i
        return lastPos==0

S=Solution()
print(S.canJump([2,3,1,1,4]))
print(S.canJump([3,2,1,0,4]))

