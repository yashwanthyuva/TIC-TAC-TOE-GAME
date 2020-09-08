from IPython.display import clear_output
def display_board(board):
    clear_output() 
    print(board[7]+"|"+board[8]+'|'+board[9])
    print("-----")
    print(board[4]+"|"+board[5]+'|'+board[6])
    print("-----")
    print(board[1]+"|"+board[2]+'|'+board[3])
def player_input():
    marker=""
    while marker!="x" and marker!="o":
        marker=input("PLAYER 1 CHOOSE WHETHER X OR O")
    player1=marker
    if player1=="x":
        player2="o"
    elif player1=="o":
        player2="x"
    else:
        pass
    return (player1,player2)
def board_input(board,marker,position):
    board[position]=marker
def win_check(board,mark):
    return  ((the_board[1]==mark and the_board[2]==mark and the_board[3]==mark) or
             (the_board[4]==mark and the_board[5]==mark and the_board[6]==mark) or
             (the_board[7]==mark and the_board[8]==mark and the_board[9]==mark) or
             (the_board[7]==mark and the_board[4]==mark and the_board[1]==mark) or
             (the_board[8]==mark and the_board[5]==mark and the_board[2]==mark) or
             (the_board[9]==mark and the_board[6]==mark and the_board[3]==mark) or
             (the_board[7]==mark and the_board[5]==mark and the_board[3]==mark) or
             (the_board[1]==mark and the_board[5]==mark and the_board[9]==mark))
import random
def choose_first():
    a=random.randint(1,2)
    if a==1:
        return 'player 1'
    else:
        return 'player 2'
def space_check(board,position):
    return board[position]==' '  
def full_board(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True
def player_choice(board):
    position=0
    while position!=[1,2,3,4,5,6,7,8,9] and not space_check(board,position):
        position=int(input("enter the position 1-9"))
    return position
def replay():
    return input("do u wanna replay (y or n)").startswith("y")
print("WELCOME TO TIC TAC TOE")
while True:
    the_board=[" "]*10
    player2_marker,player1_marker=player_input()
    turn=choose_first()
    print(f"{turn}'s first")
    play_game=input("ready to play game (yes or no)")
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False    
    while game_on==True:
        if turn=='player 1':
            display_board(the_board)
            position=player_choice(the_board)
            board_input(the_board,player1_marker,position)
            if win_check(the_board,player1_marker)==True:
                display_board(the_board)
                print("congratulations p2 has won the game")
                game_on=False
            else:
                if full_board(the_board):
                    display_board(the_board)
                    print('The game is a draw!')
                    break
                else:
                    turn ='player 2'
        elif turn=='player 2':
            display_board(the_board)
            position=player_choice(the_board)
            board_input(the_board,player2_marker,position) 
            if win_check(the_board,player2_marker)==True:
                display_board(the_board)
                print("congratulations p1 has won the game")
                game_on=False
            else:
                if full_board(the_board):
                    display_board(the_board)
                    print('The game is a draw!')
                    break
                else:
                    turn='player 1'
        else:
            pass
    if not replay():
        break