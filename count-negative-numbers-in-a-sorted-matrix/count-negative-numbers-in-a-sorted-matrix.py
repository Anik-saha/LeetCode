class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        n=len(grid[0])
        globalcount=0
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
        left=0

        for row in reversed(grid):
            right=n-1
            # print("lr",left," ",right," ",row)
            while(left<=right):
                mid=left+(right-left)//2
                # print(row[mid])
                if(row[mid]>-1):
                    left=mid+1
                else:
                    right=mid-1
            # print("After lr",left," ",right)
            if left<=n:
                globalcount+=(n-left)
        return globalcount
        