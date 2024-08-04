# https://leetcode.com/problems/pascals-triangle/
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        list1=[]
        for i in range(numRows):
            list2=[]
            for j in range(i+1):
                if j==0 or j==i:
                    list2.append(1)
                else:
                    list2.append(list1[i-1][j-1]+list1[i-1][j])
            list1.append(list2)
        return list1
            
        
