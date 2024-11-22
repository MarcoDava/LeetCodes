class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n=len(grid)
        newGrid=[([0]*(n-2)) for _ in range(n-2)]
        
        for i in range(n-2):
            for j in range(n-2):
                largestNumber=0
                for k in range(i,i+3):
                    for l in range(j,j+3):
                        if grid[k][l]>largestNumber:
                            largestNumber=grid[k][l]
                newGrid[i][j]=largestNumber
        return newGrid
