class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #initial thought process
        # we possibly need a hashmap within a hashmap or an array that stores all the possible numbers from 1-9 and add to each index according to the value, if an array index exceeeds the value of one, return False, if no value exceeds 1 per row, column and box, return True
        # the algorithm would go through each column, then rows then check the boxes
        for row in range(9):
            rowCount=set()
            for i in range(9):
                if board[row][i] in rowCount and board[row][i]!=".":
                    return False
                rowCount.add(board[row][i])

        for col in range(9):
            colCount=set()
            for i in range(9):
                if board[i][col] in colCount and board[i][col]!=".":
                    return False
                colCount.add(board[i][col])

        for i in range(3):
            for j in range(3):
                gridCount=set()
                for row in range(3):
                    for col in range(3):
                        if board[i*3+row][j*3+col] in gridCount and board[i*3+row][j*3+col] !=".":
                            return False
                        gridCount.add(board[i*3+row][j*3+col])
        return True
