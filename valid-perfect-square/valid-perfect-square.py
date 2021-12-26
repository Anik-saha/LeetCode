import numpy as np
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return int(np.sqrt(num))**2==num
#         if (num<2):
#             return num
#         left =1
#         right=num
#         while(left<right):
#             mid=left+(right-left)//2
#             if int(mid)**2==num:
#                 return mid
#             elif int(mid)**2<num:
#                 left=mid+1
#             else:
#                 right=mid-1
        
#         return 'false'
        