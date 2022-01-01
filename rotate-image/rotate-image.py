class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        length=len(matrix[0])
        n=length-1
        for i in range(length//2):
            for j in range(length-1-(i*2)):
                # print(i,j)
                # print(matrix[i][i+j],matrix[n-i-j][i],matrix[n-i][n-i-j],matrix[i+j][n-i])
                tmp=matrix[i][i+j]
                matrix[i][i+j]=matrix[n-i-j][i]
                matrix[n-i-j][i]=matrix[n-i][n-i-j]
                matrix[n-i][n-i-j]=matrix[i+j][n-i]
                matrix[i+j][n-i]=tmp
                # print(matrix[i][i+j],matrix[n-i-j][i], matrix[n-i][n-i-j],matrix[n-i-j][i])
        return matrix
            
        