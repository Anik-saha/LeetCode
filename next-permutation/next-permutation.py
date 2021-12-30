class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length=len(nums)
        index=-1
        # substring=[nums[length-1]]
        for i in range(length-2,-1,-1):
            if nums[i]<nums[i+1]:
                # print("Decreasing seq",i)
                index=i
                break
        # print(index)
        if index==-1:
            return nums.reverse()
        else:
            # print("Else")
            for i in range(length-1,index,-1):
                # print("i",i)
                if nums[i]>nums[index]:
                    # print("inside")
                    tmp=nums[i]
                    nums[i]=nums[index]
                    nums[index]=tmp
                    # print(nums[index],nums[i])
                    break

            # print("check")
            # for i in range(length):
            #     print(nums[i])
            # print("Swap")
            for i in range(index+1,(index+1+length)//2):
                # print("ins",i,nums[i],nums[length-1-i])
                tmp=nums[i]
                nums[i]=nums[length-(i-(index+1))-1]
                nums[length-(i-(index+1))-1]=tmp
                
        return nums
                
            
            
        