# https://leetcode.com/problems/find-missing-and-repeated-values/description/
 class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        arr=[]
        for i in grid:
            arr+=i
        print(arr)
        A=arr
        n=len(A)
        e1=sum(A)-((n*n+n)/2)
        x=0
        for i in A:
            x+=i*i
        e2=x-(n*(n+1)*(2*n+1)/6)
        e2=e2//e1
        ans=[int((e1+e2)//2),int((e2-e1)//2)]
        return ans

# ......................................
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        arr=[]
        for i in grid:
            arr+=i
        print(arr)
        l=[]
        d=Counter(arr)
        for i in d:
            if d[i]>1:
                l.append(i)
        for i in range(1,len(arr)+1):
            if i not in arr:
                l.append(i)
        return l
