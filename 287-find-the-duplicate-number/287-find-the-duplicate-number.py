class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Slow Pointer Fast Pointer
        # Assume distance b/w start and duplicate as x 
        # first collision at say distance a slow moved by a fast moved by 2a and cycle length =a
        # start one pointer from start and another from collision move both at same pace point of collison is duplciate
        slow=nums[0]
        fast=nums[0]
        
        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if slow == fast:
                break
        fast=nums[0]
        while slow != fast:
            slow=nums[slow]
            fast=nums[fast]
        return slow
            
            