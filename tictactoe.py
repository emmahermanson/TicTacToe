# Emma Hermanson
# 11.17.2020
# Tic Tac Toe game with 2 players
# game ends when one player wins or all boxes are filled

##################################################################################
# SET UP BOARD
# dictionary to keep track of board (len 9)
board = {'7': ' ', '8': ' ', '9': ' ',
        '4': ' ', '5': ' ', '6': ' ',
        '1': ' ', '2': ' ', '3': ' '}
        
keys = []
for key in board:
    keys.append(key)

##################################################################################
# PRINTS UPDATED BOARD
# prints updated board after every turn
def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' +  board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' +  board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' +  board['3'])
    
# board looks like:
# 7|8|9       | |
# -+-+-      -+-+-
# 4|5|6  -->  | |
# -+-+-      -+-+-
# 1|2|3       | |

##################################################################################
# GAMEPLAY
def play():
#--------------------------------------------------------------------------------#
# A PLAYER'S TURN
    #keeps track of current player's turn
    turn = 'X'
    #keeps track of total moves
    count = 0
    
    for i in range(10) :
        printBoard(board)
        print("It is player " + turn + "'s turn. Where would you like to move?")
        
        move = input()
        
        # if desired move is valid, add to board
        if (board[move] == ' '):
            board[move] = turn
            count = count+1
        # if not valid prompt to pick another square
        else:
            print("Invalid spot (already filled). Where would you like to move?")
            continue
    
        # CHECK FOR WINNER
        # check if winner after every move, after first 5 moves
        # check every possible way to win
        # all spots are the same character and not empty
        if (count >= 5):
            # across top
            if (board['7'] == board['8'] == board['9'] != ' '):
                printBoard(board)
                print("Game over. Winner: " + turn)
                break
            # across middle
            elif (board['4'] == board['5'] == board['6'] != ' '):
                printBoard(board)
                print("Game over. Winner: " + turn)
                break
            # across bottom
            elif (board['1'] == board['2'] == board['3'] != ' '):
                printBoard(board)
                print("Game over. Winner: " + turn)
                break
            # down left
            elif (board['7'] == board['4'] == board['1'] != ' '):
                printBoard(board)
                print("Game over. Winner: " + turn)
                break
            # down middle
            elif (board['8'] == board['5'] == board['2'] != ' '):
                printBoard(board)
                print("Game over. Winner: " + turn)
                break
            # down right
            elif (board['9'] == board['6'] == board['3'] != ' '):
                printBoard(board)
                print("Game over. Winner: " + turn)
                break
            # diagonal 1
            elif (board['7'] == board['5'] == board['3'] != ' '):
                printBoard(board)
                print("Game over. Winner: " + turn)
                break
            # diagonal 2
            elif (board['9'] == board['5'] == board['1'] != ' '):
                printBoard(board)
                print("Game over. Winner: " + turn)
                break
            
        # if all spots filled and no winner, declare a tie
        if (count == 9):
            print("Tie! Game over.")

        # change player after every turn
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
        
#--------------------------------------------------------------------------------#
# PLAY AGAIN ?
    restart = input("Would you like to play again? Y/N")
    
    # if answer is yes, clear board and restart gameplay
    if (restart == 'Y' or restart == 'y'):
        for key in keys:
            board[key] = ' '
        play()
        
#--------------------------------------------------------------------------------#
##################################################################################
# EXECUTE
play()
        
