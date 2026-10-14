class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        XCounter = 0
        YCounter = 0
        for i in range(len(board)):
            if not self.isValidRow(board[i]) or not self.isValidColumn(board, i):
                return False
            if not self.isValidSquare(board, XCounter, YCounter):
                return False
            if YCounter == 6:
                XCounter += 3
                YCounter = 0
            else:
                YCounter += 3
        return True  

    def isValidRow(self, rowList) -> bool:
        s = set()
        for i in rowList:
            if i == ".":
                continue
            elif i in s:
                return False
            else:
                s.add(i)
        return True

    def isValidColumn(self, board, ind) -> bool:
        s = set()
        for row in board:
            if row[ind] == ".":
                continue
            elif row[ind] in s:
                return False
            else:
                s.add(row[ind])
        return True
    
    def isValidSquare(self, board, row, column) -> bool:
        s = set()
        for i in range(3):
            for j in range(3):
                x = i + row
                y = j + column
                if board[x][y] in s:
                    return False
                if board[x][y] != ".":
                    s.add(board[x][y])
        return True
        