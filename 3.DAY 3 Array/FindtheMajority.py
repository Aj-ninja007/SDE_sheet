#https://leetcode.com/problems/majority-element/submissions/1068833522/
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d=Counter(nums)
        l=[]
        for i in d.values():
            l.append(i)
        t=max(l)
        for i in d:
            if d[i]==t:
                return i


        
