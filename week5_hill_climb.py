
import random

N = 4

def heuristic(board):
    conflicts = 0

    for i in range(N):
        for j in range(i + 1, N):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1

    return conflicts


def hill_climbing():
    board = [random.randint(0, N - 1) for _ in range(N)]

    while True:
        current_h = heuristic(board)

        if current_h == 0:
            return board

        best_board = board[:]
        best_h = current_h

        for col in range(N):
            for row in range(N):
                if board[col] != row:
                    new_board = board[:]
                    new_board[col] = row

                    h = heuristic(new_board)

                    if h < best_h:
                        best_h = h
                        best_board = new_board

        if best_h >= current_h:
            return None

        board = best_board


def print_board(board):
    if board is None:
        print("Local optimum reached. No solution found.")
        return

    for row in range(N):
        for col in range(N):
            if board[col] == row:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()

    print("Solution found!")


# Repeat until a solution is found
while True:
    solution = hill_climbing()
    if solution is not None:
        break

print_board(solution)
