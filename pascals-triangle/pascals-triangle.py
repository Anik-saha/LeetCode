class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal_list=[[1]]
        for i in range(1,numRows):
            pascal_list.append([1]*(i+1))
            for j in range(1,i):
                pascal_list[i][j]=pascal_list[i-1][j-1]+pascal_list[i-1][j]
        return pascal_list
            