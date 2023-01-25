import random, copy, math


class T3Board:
    board = []
    
    def __init__(self):
        self.board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        
    def empty_positions(self):
        return [i for i in self.board if i not in "XO"]
    
    def check_win_terminal(self):
        win_lines = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
        for win_line in win_lines:
            if self.board[win_line[0]] ==  self.board[win_line[1]] == self.board[win_line[2]]:
                return {'win': self.board[win_line[0]], 'terminal': True}
        if len(self.empty_positions()) == 0:
            return {'win': 'D', 'terminal': True}
        return {'win': '-', 'terminal': False}

    def play(self, mark: str, pos: str):
        un_played = self.empty_positions()
        if pos in un_played and mark in 'XO':
            self.board[int(pos)-1] = mark
            return True
        else:
            return False

    def undo_play(self, pos: str):
        if self.board[int(pos) - 1] in 'XO':
            self.board[int(pos)-1] = pos
        return

    def show(self, show_numbers = False):
        lines = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        print()
        if show_numbers:
            for line in lines:
                print(' '+self.board[line[0]], self.board[line[1]], self.board[line[2]],sep=' | ')
                if line[0] < 6:
                    print('---+---+---')
        else:
            for line in lines:
                print(' '+self.board[line[0]] if self.board[line[0]] in 'XO' else '  ',
                      self.board[line[1]] if self.board[line[1]] in 'XO' else ' ',
                      self.board[line[2]] if self.board[line[2]] in 'XO' else ' ',sep=' | ')
                if line[0] < 6:
                    print('---+---+---')
        return

    def select_location(self, mark: str):
        move_location: str = '0'
        input_prompt = 'Choose 1 to 9 for player - ' + mark + ': '
        while move_location not in self.empty_positions():
            move_location = input(input_prompt)
        return move_location

    def minimax(self, mark, lvl, is_max):
        if self.check_win_terminal()['terminal']:
            if self.check_win_terminal()['win'] == 'O':
                return 10
            elif self.check_win_terminal()['win'] == 'X':
                return -10
            elif self.check_win_terminal()['win'] == 'D':
                return 0
        if is_max:
            best_score = -1000
            level = 0
            for next_level_move in self.empty_positions():
                self.play('O', next_level_move)
                cbm_score = self.minimax('X', level+1, False)
                self.undo_play(next_level_move)
                best_score = max(cbm_score, best_score)
            return best_score
        else:  # mark is X - simulated human player
            best_score = 1000
            level = 0
            for next_level_move in self.empty_positions():
                self.play('X', next_level_move)
                cbm_score = self.minimax('O', level+1, True)
                self.undo_play(next_level_move)
                best_score = min(cbm_score, best_score)
            return best_score

    def computer_best_move(self):
        best_score = -1000
        best_move = '0'
        level = 0
        for next_level_move in self.empty_positions():
            self.play('O', next_level_move)
            cbm_score = self.minimax('O', level+1, False)
            self.undo_play(next_level_move)
            if cbm_score > best_score:
                best_score = cbm_score
                best_move = next_level_move
        return best_move


# MAIN CODE
player_mark = 'X'  # begin with the human player
game = T3Board()  # initialise the board
game.show(show_numbers=True)
while len(game.empty_positions()) > 0:
    if len(game.empty_positions()) == 1:
        last_move = game.empty_positions()[0]
        game.play(player_mark, last_move)
        print('Automatically playing the last move -', last_move)
    elif player_mark == 'X':  # person playing
        game.play(player_mark, game.select_location(player_mark))
    else:  # computer playing
        o_move = game.computer_best_move()
        game.play(player_mark, o_move)
        print('Computer is choosing where to go -',o_move)
    if game.check_win_terminal()['terminal']:
        game.show()
        break  # stop turns if the game is terminal
    game.show()
    player_mark = 'O' if player_mark == 'X' else 'X'

print('Drawn game' if game.check_win_terminal()['win'] == 'D' else 'Winner is ' + game.check_win_terminal()['win'])
