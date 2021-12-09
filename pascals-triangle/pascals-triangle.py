class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Using Lambda function and map 
        pascal_list=[[1]]
        for i in range(1,numRows):
            pascal_list +=[list(map(lambda x,y:x+y,[0]+pascal_list[i-1],pascal_list[i-1]+[0]))]
        return pascal_list
            
        