#Writing a funtion which can print out a 3 by 3 board representation
def display_board(board):
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])

#Writing function that can take in a player input and assign their marker as 'X' or 'O'
def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')
    
#Writing a function that takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board.
def place_marker(board, marker, position):
    board[position] = marker
    
#Writing a function that takes in a board and checks to see if someone has won
def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal
  
#Writing a function that uses the random module to randomly decide which player goes first.
import random
def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'
    
#Writing a function that returns a boolean indicating whether a space on the board is freely available.
def space_check(board, position):
    return board[position] == ' '

#Write a function that checks if the board is full and returns a boolean value. True if full, False otherwise
    def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

#Writing a function that asks for a player's next position (as a number 1-9) and then uses the function from step 6 to check if its a free position. If it is, then returns the position.
def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
    return position

#Writing a function that asks the player if they want to play again and returns a boolean True if they do want to play again.
def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


     
