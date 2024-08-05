#https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans=[intervals[0]]
        n=len(intervals)
        j=0
        for i in range(1,n):
            if ans[j][1]>=intervals[i][0]:
                ans[j][1]=max(intervals[i][1],ans[j][1])
            else:
                j+=1
                ans.append(intervals[i])
        return ans

        
