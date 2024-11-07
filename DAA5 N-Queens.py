# def is_safe(board,row,col):

#     for i in range(col):
#         if board[row][i]==1:
#             return False

#     for i,j in zip(range(row,-1,-1), range(col,-1,-1)):
#         if board[i][j] == 1:
#             return False
        
#     for i,j in zip(range(row,N,1), range(col,-1,-1)):
#         if board[i][j]==1:
#             return False

#     return True

# def util(board, col):

#     if col >= N:
#         return True

#     for i in range(N):

#         if is_safe(board,i,col):

#             board[i][col] = 1

#             if util(board,col+1)==True:
#                 return True

#             board[i][col] = 0

#     return False

# N = 8

# board = [[0 for i in range(N)] for i in range(N)]

# if util(board, 0) == False:
#     print ("Solution does not exist")
    
# for i in range(N):
#     for j in range(N):
#         if board[i][j] == 1:
#             print("Q", end=" ")
#         else:
#             print("-", end=" ")
#     print()

# """
# Output:

# Q - - - - - - - 
# - - - - - - Q -
# - - - - Q - - -
# - - - - - - - Q
# - Q - - - - - -
# - - - Q - - - -
# - - - - - Q - -
# - - Q - - - - -

# """



def solve_n_queens(n):
    def is_safe(board, row, col):
        # Check if there's a queen in the same column
        for i in range(row):
            if board[i] == col:
                return False
        
        # Check upper left diagonal
        for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
            if board[i] == j:
                return False

        # Check upper right diagonal
        for i, j in zip(range(row - 1, -1, -1), range(col + 1, n)):
            if board[i] == j:
                return False

        return True

    def backtrack(row):
        # If we've placed queens in all rows, add the solution
        if row == n:
            solution = []
            for i in range(n):
                line = " - " * board[i] + "Q" + " - " * (n - board[i] - 1)
                solution.append(line)
            solutions.append(solution)
            return

        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1

    solutions = []
    board = [-1] * n  # -1 indicates no queen is placed in the row
    backtrack(0)
    return solutions

# Example usage:
n = 8
solutions = solve_n_queens(n)
for solution in solutions:
    for line in solution:
        print(line)
    print()

print(len(solutions))