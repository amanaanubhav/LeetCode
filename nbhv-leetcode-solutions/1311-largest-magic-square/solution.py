class Solution:
    def largestMagicSquare(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        row_pref = [[0] * (cols + 1) for _ in range(rows)]
        col_pref = [[0] * (cols) for _ in range(rows + 1)]
        
        for r in range(rows):
            for c in range(cols):
                row_pref[r][c+1] = row_pref[r][c] + grid[r][c]
                col_pref[r+1][c] = col_pref[r][c] + grid[r][c]
        
        def is_magic(r, c, k):

            target = row_pref[r][c+k] - row_pref[r][c]
            
            for i in range(r + 1, r + k):
                if row_pref[i][c+k] - row_pref[i][c] != target:
                    return False
            
            for j in range(c, c + k):
                if col_pref[r+k][j] - col_pref[r][j] != target:
                    return False
            
            diag_sum = 0
            for i in range(k):
                diag_sum += grid[r+i][c+i]
            if diag_sum != target:
                return False
                
            anti_diag_sum = 0
            for i in range(k):
                anti_diag_sum += grid[r+i][c+k-1-i]
            return anti_diag_sum == target

        for k in range(min(rows, cols), 1, -1):
            for r in range(rows - k + 1):
                for c in range(cols - k + 1):
                    if is_magic(r, c, k):
                        return k
        
        return 1
