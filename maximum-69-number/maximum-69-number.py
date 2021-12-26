class Solution:
    def maximum69Number (self, num: int) -> int:
        # return int(str(num).replace('6','9',1))
        i=1000
        while (i>=1):
            print(int(num//i))
            print(int(num//(i*10))*10)
            if int(num//i)-int((num//(i*10)))*10==6:
                return int(num+i*3)
            i/=10
        return int(num)
        
        