#https://leetcode.com/problems/majority-element-ii/

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)//3
        l=[]
        d=Counter(nums)
        for i in d:
            if d[i]>len(nums)//3:
                l.append(i)        
        return l
        
