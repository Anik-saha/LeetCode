class Solution:
    def setZeroes(self, Matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        No_Of_rows=len(Matrix)
        No_Of_cols=len(Matrix[0])
        First_row_zero=any(Matrix[0][i]==0 for i in range(No_Of_cols))
        First_col_zero=any(Matrix[i][0]==0 for i in range(No_Of_rows))

        for i in range(1,No_Of_rows):
            for j in range(No_Of_cols):
                if Matrix[i][j]==0:Matrix[i][0]=Matrix[0][j]=0
        
        # for i in range(No_Of_rows):
        #     for j in range(No_Of_cols):
        #         print(Matrix[i][j],end='')
        #     print()
       
        for i in range(1,No_Of_rows):
            for j in range(1,No_Of_cols):
                if Matrix[i][0]*Matrix[0][j]==0:Matrix[i][j]=0
               
        if First_row_zero:
            for i in range(No_Of_cols):
                Matrix[0][i]=0
                
        if First_col_zero:
            for i in range(No_Of_rows):
                Matrix[i][0]=0
        
                
        
        
        
        