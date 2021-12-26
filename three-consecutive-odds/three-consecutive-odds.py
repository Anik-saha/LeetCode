class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count=0
        for ele in arr:
            if ele%2==1:
                count+=1
            else:
                count=0
            print(count)
            if (count==3):
                # print(count)
                return True
        return False
        