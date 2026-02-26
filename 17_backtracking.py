"""
BACKTRACKING - Try all possibilities

THEORY:
- Brute force with pruning
- Build solution incrementally
- Abandon solution if it can't lead to valid answer
- Uses recursion to explore all paths

APPROACH:
1. Choose - Make a choice
2. Explore - Recursively explore with that choice
3. Unchoose - Backtrack if doesn't work

TEMPLATE:
```
def backtrack(path, choices):
    if is_solution(path):
        result.append(path)
        return
    for choice in choices:
        if is_valid(choice):
            make_choice(choice)
            backtrack(path, remaining_choices)
            undo_choice(choice)  # Backtrack
```

TIME COMPLEXITY: Often exponential O(b^d)
- b = branching factor
- d = depth

OPTIMIZATION:
- Pruning - Skip invalid branches early
- Constraint propagation
- Heuristics for choice ordering

COMMON PROBLEMS:
1. N-Queens - Place queens on chessboard
2. Sudoku Solver - Fill grid with constraints
3. Permutations - All arrangements
4. Combinations - All selections
5. Subset Sum - Find subset with target sum
6. Word Search - Find word in grid
7. Rat in Maze - Find path

WHEN TO USE:
- Need all solutions
- Constraint satisfaction
- Combinatorial problems
"""

def n_queens(n):
    def is_safe(board, row, col):
        for i in range(row):
            if board[i] == col or abs(board[i] - col) == abs(i - row):
                return False
        return True
    
    def solve(board, row):
        if row == n:
            result.append(board[:])
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                solve(board, row + 1)
                board[row] = -1
    
    result = []
    solve([-1] * n, 0)
    return result

def sudoku_solver(board):
    def is_valid(board, row, col, num):
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if board[start_row + i][start_col + j] == num:
                    return False
        return True
    
    def solve():
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    for num in range(1, 10):
                        if is_valid(board, i, j, num):
                            board[i][j] = num
                            if solve():
                                return True
                            board[i][j] = 0
                    return False
        return True
    
    solve()
    return board

def permutations(arr):
    result = []
    def backtrack(path, remaining):
        if not remaining:
            result.append(path[:])
            return
        for i in range(len(remaining)):
            backtrack(path + [remaining[i]], remaining[:i] + remaining[i+1:])
    backtrack([], arr)
    return result

def combinations(n, k):
    result = []
    def backtrack(start, path):
        if len(path) == k:
            result.append(path[:])
            return
        for i in range(start, n + 1):
            path.append(i)
            backtrack(i + 1, path)
            path.pop()
    backtrack(1, [])
    return result

def word_search(board, word):
    def dfs(i, j, k):
        if k == len(word):
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[k]:
            return False
        temp = board[i][j]
        board[i][j] = '#'
        found = dfs(i+1, j, k+1) or dfs(i-1, j, k+1) or dfs(i, j+1, k+1) or dfs(i, j-1, k+1)
        board[i][j] = temp
        return found
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if dfs(i, j, 0):
                return True
    return False

if __name__ == "__main__":
    print(f"N-Queens(4): {len(n_queens(4))} solutions")
    print(f"Permutations: {permutations([1, 2, 3])}")
    print(f"Combinations C(4,2): {combinations(4, 2)}")
