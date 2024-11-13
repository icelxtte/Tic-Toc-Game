'''Programmer: Sachorra Douglas
Date: 10/24/2024
Assignment: Python_Project 1
'''

board = [" "] * 10  # Initialize the board with empty spaces

def draw_board(board):
    print(board[7] + "|" + board[8] + "|" + board[9])
    print("--+--+--")
    print(board[4] + "|" + board[5] + "|" + board[6])
    print("--+--+--")
    print(board[1] + "|" + board[2] + "|" + board[3])

player1 = input("Enter 1st Player name: ")
player2 = input("Enter 2nd Player name: ")

print(f"{player1}: X ; {player2}: O")

def game():
    turn = "X"
    count = 0
    player_turn = player1

    for i in range(10):
        draw_board(board)
        print("It's your turn, " + player_turn + ". Move to which place?")

        move = int(input())  # Changed from eval() to int() for safety

        if board[move] == " ":
            board[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue

        if count >= 5:
            if board[7] == board[8] == board[9] != " " or \
               board[4] == board[5] == board[6] != " " or \
               board[1] == board[2] == board[3] != " " or \
               board[1] == board[4] == board[7] != " " or \
               board[2] == board[5] == board[8] != " " or \
               board[3] == board[6] == board[9] != " " or \
               board[7] == board[5] == board[3] != " " or \
               board[1] == board[5] == board[9] != " ":
                declare_winner(turn)
                break

        if count == 9:
            print("\nGame Over.\n")
            print("It's a Tie!!")

        if turn == "X":
            turn = "O"
            player_turn = player2
        else:
            turn = "X"
            player_turn = player1

def declare_winner(turn):
    draw_board(board)
    print("\nGame Over.\n")
    if turn == "X":
        print(f" **** {player1} won ****")
    else:
        print(f" **** {player2} won ****")

restart = input("\nDo you want to play Again? (y/n):")
if restart.lower() == "y":
    for element in range(len(board)):
        board[element] = " "  # Reset the board to empty
    game()
