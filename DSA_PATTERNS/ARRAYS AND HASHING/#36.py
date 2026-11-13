class Solution(object):
    def isvalidsudoku(self, board):
        
        for i in range(len(board)):
            row = set()
            for j in range(len(board)):
                if board[i][j] == ".":
                    continue
                elif board[i][j] in row:
                    return False
                else:
                    row.add(board[i][j])
                
        for i in range(len(board)):
            column = set()
            for j in range(len(board)):
                if board[j][i] == ".":
                    continue
                elif board[j][i] in column:
                    return False
                else:
                    column.add(board[j][i])

        for i in range(0,9,3):
            for j in range(0,9,3):
                box = set()
                for k in range(i ,i+3):
                    for m in range(j ,j+3):
                        if board[k][m] == ".":
                            continue
                        elif board[k][m] in box:
                            return False
                        else:
                            box.add(board[k][m])
                
        return True

board = []
for i in range(9):
    row = input("enter the 9 value with space:").split()
    board.append(row)
sol = Solution()
result = sol.isvalidsudoku(board)
print(result)