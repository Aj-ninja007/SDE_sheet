# https://leetcode.com/problems/maximum-subarray/description/
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curS=nums[0]
        maxS=curS
        for i in range(1,len(nums)):
            maxS=max(maxS+nums[i],nums[i])
            curS=max(maxS,curS)
        return curS

        


        
