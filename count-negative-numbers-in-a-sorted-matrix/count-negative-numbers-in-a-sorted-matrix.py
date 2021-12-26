class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
#         Solution 1
#         n=len(grid[0])
#         globalcount=0
#         for row in grid:
#             left=0
#             right=n-1
            
#             while(left<=right):
#                 mid=left+(right-left)//2
#                 # print(row[mid])
#                 if(row[mid]>-1):
#                     left=mid+1
#                 else:
#                     right=mid-1
#             if left<=n:
#                 globalcount+=(n-left)
#         return globalcount
        
    
        # Solution 2
        # left=0
        # for i in range(len(grid)-1,-1,-1):
        #     right=n-1
        #     while(left<=right):
        #         mid=left+(right-left)//2
        #         if(grid[i][mid]>-1):
        #             left=mid+1
        #         else:
        #             right=mid-1
        #     if left<=n:
        #         globalcount+=(n-left)
        # return globalcount
        
            # def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        r, c, cnt = 0, n - 1, 0
        while r < m and c >= 0:
            if grid[r][c] < 0:
                cnt += m - r
                c -= 1
            else:
                r += 1
        return cnt