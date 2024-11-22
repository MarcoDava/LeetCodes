class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        sum=0
        n=len(grid)
        m=len(grid[0])
        for k in range(n):
            if grid[k][0]==0:
                for l in range(m):
                    if grid[k][l]==0:
                        grid[k][l]=1
                    else:
                        grid[k][l]=0
        for i in range(1,m):
            zerocount=0
            for j in range(n):
                if grid[j][i]==0:
                    zerocount+=1
            if zerocount>(n//2):
                for j in range(n):
                    if grid [j][i]==0:
                        grid[j][i]=1
                    else:
                        grid[j][i]=0

        for k in range(n):
            rowsum=0
            for l in range(m):
                if grid[k][l]==1:
                    rowsum+=2**(m-l-1)
            sum+=rowsum
        return sum
