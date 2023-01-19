import copy

def show_board(board):
    print(' '.join(board[0:3]) + "\n" + ' '.join(board[3:6]) + "\n" + ' '.join(board[6:9]))


def choose_location(board,idx,move_letter):
    remaining = remaining_moves(board)
    if idx in remaining:
        board[int(idx) - 1] = move_letter
        return True
    else:
        return False


def game_state(board):
    possible_wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for indexes in possible_wins:
        if board[indexes[0]] == board[indexes[1]] == board[indexes[2]]:
            return board[indexes[0]]
    remaining = remaining_moves(board)
    return '-' if len(remaining) != 0 else 'D'


def remaining_moves(board):
    full_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    remaining = [i for i in board if i in full_list]
    return remaining


def random_turn(board):
    import random
    remaining = remaining_moves(board)
    return random.choice(remaining)


def mini_max(board,player_sign,max_or_min):
    cp_board = copy.deepcopy(board)
    remaining = remaining_moves(cp_board)
    mm_res_dict = {'X': -10, 'D': 0, 'O': 10} if player_sign == 'O' else {'X': 10, 'D': 0, 'O': -10}
    for play in remaining:
        choose_location(cp_board, int(play)-1, player_sign)
        mm_state = game_state(cp_board)
        if mm_state in 'XDO':
            return mm_res_dict[mm_state]
        next_player = 'X' if player_sign == 'O' else 'O'
        mm_maxmin = 'min' if max_or_min == 'max' else 'max'
        mini_max(cp_board,next_player,mm_maxmin)


game_board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
moves_made, player = 0, 'X'
show_board(game_board)
while moves_made < 9:
    while True:
        if player == 'X':
            location_str = input('type the number of the turn for ' + player + ' ')
        else:
            location_str = random_turn(game_board)
            print("the computer is selecting a position")
        valid_move = choose_location(game_board,location_str,player)
        if valid_move:
            player = 'O' if player == 'X' else "X"
            moves_made += 1
            break
    show_board(game_board)
    state_of_play = game_state(game_board)
    if state_of_play in 'XOD':
        break
game_result = 'The winner is ' + state_of_play if state_of_play in 'XO' else "This game is a draw"
print(game_result)
