from board import AI, HUMAN, EMPTY

# Depth limit (controls thinking time)
MAX_DEPTH = 3


def minimax(board, depth, isMax, alpha, beta):

    score = board.evaluate()

    # Terminal states
    if score == 10:
        return score - depth

    if score == -10:
        return score + depth

    if not board.is_moves_left():
        return 0

    # Depth limit reached → use heuristic
    if depth >= MAX_DEPTH:
        return board.heuristic()

    # AI (Maximizer)
    if isMax:
        best = -1000

        for i in range(4):
            for j in range(4):
                if board.board[i][j] == EMPTY:
                    board.board[i][j] = AI

                    value = minimax(board, depth + 1, False, alpha, beta)

                    board.board[i][j] = EMPTY
                    best = max(best, value)
                    alpha = max(alpha, best)

                    # Alpha-Beta pruning
                    if beta <= alpha:
                        return best

        return best

    # Human (Minimizer)
    else:
        best = 1000

        for i in range(4):
            for j in range(4):
                if board.board[i][j] == EMPTY:
                    board.board[i][j] = HUMAN

                    value = minimax(board, depth + 1, True, alpha, beta)

                    board.board[i][j] = EMPTY
                    best = min(best, value)
                    beta = min(beta, best)

                    # Alpha-Beta pruning
                    if beta <= alpha:
                        return best

        return best


def find_best_move(board):
    best_val = -1000
    best_move = (-1, -1)

    for i in range(4):
        for j in range(4):
            if board.board[i][j] == EMPTY:
                board.board[i][j] = AI

                move_val = minimax(board, 0, False, -1000, 1000)

                board.board[i][j] = EMPTY

                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    return best_move
