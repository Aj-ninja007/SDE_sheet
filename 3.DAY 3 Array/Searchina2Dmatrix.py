#https://leetcode.com/problems/search-a-2d-matrix/
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        res=[]
        for i in matrix:
            res+=i
        for i in res:
            if target in res:
                return True
        return False
