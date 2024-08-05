Find the duplicate in an array of N+1 integers#
#https://leetcode.com/problems/find-the-duplicate-number/description/
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d=Counter(nums)
        for i in d:
            if d[i]>=2:
                return i
        
       
        

       
