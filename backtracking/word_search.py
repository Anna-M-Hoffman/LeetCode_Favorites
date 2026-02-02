# WORD SEARCH
# Given a 2-D grid of characters board and a string word, return true if 
#the word is present in the grid, otherwise return false.

# For the word to be present it must be possible to form it with a path in 
# the board with horizontally or vertically neighboring cells. 
# The same cell may not be used more than once in a word.

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()
        # r is current row, c is current column, and i is
        # the index of the letter in the word being searched
        def dfs(r, c, i):
            # If all the letters have been found
            if len(path) == len(word):
                return True

            # The conditions where the tile cannot be used
            if (r < 0 or c < 0 or  # Out of bounds
                r >= ROWS or c >= COLS or # Out of bounds
                board[r][c] != word[i] or # No match
                (r, c) in path): # Tile already added to path
                return False
                                                                            
            path.add((r, c)) 

            res = (dfs(r + 1, c, i + 1) or # Down
            dfs(r - 1, c, i + 1) or # Up
            dfs(r, c + 1, i + 1) or # Right
            dfs(r, c - 1, i + 1)) # Left
                            
            path.remove((r, c)) # Backtracking means removing letters
            # after all paths are explored from it so other paths can use it

            return res # Will return True if any recursive direction returns True

        # Go through the entire board and run dfs on each tile
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0): # Performs dfs with every tile (r, c) as the start until
                    return True # True returns, menaing the word was found
        return False # Word was not found and entire grid was searched
