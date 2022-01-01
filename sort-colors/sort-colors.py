class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low=0
        high=len(nums)-1
        counter=0        
        while(counter <=high):
            if nums[counter]==0:
                nums[low],nums[counter]=nums[counter],nums[low]
                low+=1
                counter+=1
            elif nums[counter]==2:
                nums[high],nums[counter]=nums[counter],nums[high]
                high-=1
                # counter+=1
            else:
                counter+=1
            print(counter,low,high,nums)
        return nums