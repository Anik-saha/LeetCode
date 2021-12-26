class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxval=-1
        for i in range(len(arr)-1,-1,-1):
            arr[i],maxval=maxval,max(maxval,arr[i])
            
        return arr