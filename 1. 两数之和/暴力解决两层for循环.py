
# https://leetcode-cn.com/problems/two-sum/
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    # 暴力解决
    length=len(nums)
    for i in range (0,length):
        for j in range (i+1,length):
            if(nums[i]+nums[j] == target):
                return [ i , j]
    return [-1,-1]

# class Solution {
#     public int[] twoSum(int[] nums, int target) {
#         //暴力解决

#         for(int i=0 ; i < nums.length ; i++){
#             for(int j = i+1 ; j < nums.length ; j++){
#                 if(nums[i]+nums[j] == target){
#                     return new int[] { i , j};
#                 }
#             }
#         }
#         return new int[] { -1 , -1};
#     }
# }

if __name__ == '__main__':
    print(twoSum([2,7,11,15],9))
