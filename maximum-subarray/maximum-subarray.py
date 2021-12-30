import math
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        local_sum=0
        max_sum=-math.inf
        for ele in nums:
            local_sum+=ele
            max_sum=max(local_sum,max_sum)
            if local_sum<=0:
                local_sum=0
        return max_sum
        