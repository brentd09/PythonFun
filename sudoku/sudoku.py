import inspect

class SudokuCell:
    def __init__(self, val, pos):
        self.number = val
        self.index = pos
        self.col = pos % 9
        self.row = int(pos / 9)
        self.box = (int(int(pos / 9) / 3) * 3) + (int((pos % 9) / 3))
        self.possible = ['1','2','3','4','5','6','7','8','9'] if val not in '123456789' else val

    def set_value(self,val):
        self.number = val
        self.possible = list(val)


class SudokuGame:
    def __init__(self,board):
        self.board = board

    def unsolved(self):
        return [i for i in self.board if i.number not in '123456789']

    def solved(self):    
        return [i for i in self.board if i.number in '123456789']

    def show_board(self):
        count_row = 0
        count_col = 0
        for shift in range(0,80,9):
            count_row += 1
            for i in range(9):
                count_col += 1
                print(self.board[i + shift].number,end = '  ')
                if count_col % 3 == 0:
                    print('  ',end='')
            print("\n") if count_row % 3 == 0 else print()    

    def solve_naked_single(self, pos):
        full_set = {'1','2','3','4','5','6','7','8','9'}
        if self.board[pos].number not in '123456789':
            related_row = [i for i in self.board if i.row == self.board[pos].row]
            related_col = [i for i in self.board if i.col == self.board[pos].col]
            related_box = [i for i in self.board if i.box == self.board[pos].bos]
            all_related_obj = related_row + related_col + related_box
            all_related_numbers = [i.number for i in all_related_obj if i.number in '123456789']
            all_unique_numbers = list(set(all_related_numbers))
            set_unique_numbers = set(all_unique_numbers)
            if len(all_unique_numbers) == 8:
                diff_sets = set_unique_numbers.symmetric_difference(full_set)
                if len(diff_sets) == 1:
                    self.board[pos].set_value(diff_sets[0])
                    return True
        return False            


# MAIN CODE
# initial_board = '--68----33------51--134--------1----9-5--734-6--25-1-7--45----95----2-------79-8-'
initial_board = '31-7592-625-----9-87-6-3451---96--34--5--8----3----6-8-912-6----6-----4---358-1--'


game_list = []
for i in range(81):
    game_list.append(SudokuCell(initial_board[i],i))

game = SudokuGame(game_list)
game.show_board()
unsolved = [i for i in game.unsolved]
for cell_unsolved in unsolved:
    naked_single_solved = game.solve_naked_single(cell_unsolved.index)
    if naked_single_solved:
        game.show_board
