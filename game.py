from board import Board, HUMAN, AI
from minimax import find_best_move


def main():
    game = Board()

    print("===== 4x4 TIC TAC TOE =====")
    print("You are X | AI is O")
    print("Enter values between 0 and 3")

    while True:
        game.print_board()

        # Human move
        try:
            r = int(input("Enter row (0-3): "))
            c = int(input("Enter col (0-3): "))

            if r not in range(4) or c not in range(4):
                print("Invalid position!")
                continue

            if game.board[r][c] != " ":
                print("Cell already occupied!")
                continue

            game.board[r][c] = HUMAN

        except:
            print("Invalid input! Enter numbers only.")
            continue

        # Human win check
        if game.evaluate() == -10:
            game.print_board()
            print("🎉 You Win!")
            break

        if not game.is_moves_left():
            game.print_board()
            print("It's a Draw!")
            break

        # AI move
        print("\nAI is thinking...\n")
        move = find_best_move(game)
        game.board[move[0]][move[1]] = AI

        # AI win check
        if game.evaluate() == 10:
            game.print_board()
            print(" AI Wins!")
            break

        if not game.is_moves_left():
            game.print_board()
            print("It's a Draw!")
            break


if __name__ == "__main__":
    main()
