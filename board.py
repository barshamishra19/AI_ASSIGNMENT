EMPTY = " "
HUMAN = "X"
AI = "O"

class Board:
    def __init__(self):
        self.board = [[EMPTY for _ in range(4)] for _ in range(4)]

    def print_board(self):
        print("\nCurrent Board State:\n")
        for row in self.board:
            print(" | ".join(row))
            print("-" * 13)

    def is_moves_left(self):
        for row in self.board:
            if EMPTY in row:
                return True
        return False

    # Win/Loss evaluation
    def evaluate(self):

        # Rows
        for i in range(4):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] == self.board[i][3] != EMPTY:
                return 10 if self.board[i][0] == AI else -10

        # Columns
        for j in range(4):
            if self.board[0][j] == self.board[1][j] == self.board[2][j] == self.board[3][j] != EMPTY:
                return 10 if self.board[0][j] == AI else -10

        # Diagonal 1
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == self.board[3][3] != EMPTY:
            return 10 if self.board[0][0] == AI else -10

        # Diagonal 2
        if self.board[0][3] == self.board[1][2] == self.board[2][1] == self.board[3][0] != EMPTY:
            return 10 if self.board[0][3] == AI else -10

        return 0

    # Heuristic evaluation (VERY IMPORTANT for speed)
    def heuristic(self):
        score = 0
        lines = []

        # Rows
        for i in range(4):
            lines.append(self.board[i])

        # Columns
        for j in range(4):
            col = [self.board[i][j] for i in range(4)]
            lines.append(col)

        # Diagonals
        lines.append([self.board[i][i] for i in range(4)])
        lines.append([self.board[i][3-i] for i in range(4)])

        for line in lines:
            ai_count = line.count(AI)
            human_count = line.count(HUMAN)

            # Favor AI lines
            if ai_count > 0 and human_count == 0:
                score += ai_count * 3

            # Penalize human threats
            if human_count > 0 and ai_count == 0:
                score -= human_count * 3

        return score
