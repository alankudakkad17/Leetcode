class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row = len(board)
        col = len(board[0])

        def dfs(r, c):

            if r < 0 or r >= row or c < 0 or c >= col:
                return

            if board[r][c] != "O":
                return

            board[r][c] = "T"

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        for r in range(row):
            for c in range(col):

                if r == 0 or r == row - 1 or c == 0 or c == col - 1:
                    dfs(r, c)

        for r in range(row):
            for c in range(col):

                if board[r][c] == "O":
                    board[r][c] = "X"

                elif board[r][c] == "T":
                    board[r][c] = "O"
        
