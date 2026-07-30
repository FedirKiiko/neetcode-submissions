class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        validRows = True
        validColumn = True
        validBox = True

        # Checking rows for equalities
        for row in board:
            total = []
            unique = set()
            for num in row:
                if num.isdigit():
                    total.append(num)
                    unique.add(num)               
            if len(unique) != len(total):
                validRows = False

        # Checking columns for equalities
        for i in range(9):
            total = []
            unique = set()
            for j in range(9):
                if board[j][i].isdigit():
                    total.append(board[j][i])
                    unique.add(board[j][i])
            if len(unique) != len(total):
                validColumn = False


        # Checking boxes for equalities
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                total = []
                unique  = set()
                for x in range(3):
                    for y in range(3):
                        if board[i+x][j+y].isdigit():
                            total.append(board[i+x][j+y])
                            unique.add(board[i+x][j+y])
                if len(unique) != len(total):
                    validBox = False
                    

        return validRows and validColumn and validBox
