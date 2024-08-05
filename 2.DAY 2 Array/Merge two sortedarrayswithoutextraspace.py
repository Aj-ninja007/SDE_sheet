#https://leetcode.com/problems/merge-sorted-array/description/
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        j=0
        for i in range(n+m):
            if nums1[i]==0 and n>j:
                nums1[i]=nums2[j]
                j+=1
        return nums1.sort()

         
        

        
