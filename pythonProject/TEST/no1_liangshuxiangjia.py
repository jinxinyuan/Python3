class Solution(object):
    def twoSum(self, nums, target):
        length=len(nums)
        for i in range (0,length):
            for j in range (i+1,length):
                if(nums[i]+nums[j] == target):
                    return [ i , j]
        return [-1,-1]

