import random
def display_board(board):
    print('\n'*50)
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('- - -')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('- - -')
    print(board[1]+'|'+board[2]+'|'+board[3])

def player_input():
    
    marker = ''
    
    while marker != 'x' and marker !='o':
        marker = input('Player1: Choose x or o: ')
    if marker == 'x':
        return ('x', 'o')
    else:
        return ('o', 'x')

def win_check(board, mark):


    return ((board[7] == board[8] == board[9] == mark) or 
    (board[4] == board[5] == board[6] == mark) or
    (board[3] == board[2] == board[1] == mark) or
    (board[7] == board[5] == board[3] == mark) or
    (board[7] == board[4] == board[1] == mark) or
    (board[2] == board[5] == board[8] == mark) or
    (board[3] == board[6] == board[9] == mark) or
    (board[1] == board[5] == board[9] == mark))

def choose_first():
    flip = random.randint(0, 1)

    if flip == 0:
        return 'player1'
    else:
        return 'player2'

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):

    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose a position: (1-9)'))
    return position

def replay():
    result = input('play again?(y/n)')
    return result == 'y'


#-----------MainFunction-----------

print("***Welcome***")
repeat = True
the_board = [' ']*10
while repeat:
    player1_marker, player2_marker = player_input()

    turn = choose_first()
    print(turn + ' will move')

    play_game = input('Ready to play? (y/n)')
    game_on = play_game == 'y'

    while game_on:
        if turn == 'player1':
            display_board(the_board)
            position = player_choice(the_board)
            the_board[position] = player1_marker
            
            if win_check(the_board, player1_marker):
                print(win_check(the_board, player1_marker))
                display_board(the_board)
                print('PLAYER1 HAS WON!!!!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board()
                    print('TIE GAME!')
                    game_on = False
                else:
                    turn = 'player2'

        else:
            display_board(the_board)
            position = player_choice(the_board)
            the_board[position] = player2_marker

            if win_check(the_board,player2_marker):
                display_board(the_board)
                print('PLAYER2 HAS WON!!!!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board()
                    print('TIE GAME!')
                    game_on = False
                else:
                    turn = 'player1'
    repeat = replay()