#! /usr/bin/env python

class SymbolEnum:
    def __init__(self):
        self.__zero = 'O'
        self.__cross = 'X'
        self.__zero_line = self.__zero + self.__zero + self.__zero
        self.__cross_line = self.__cross + self.__cross + self.__cross
        self.__unfinished = 'u'
        self.__draw = 'd'
    @property
    def unfinished(self):
        return self.__unfinished
    @property
    def zero(self):
        return self.__zero
    @property
    def cross(self):
        return self.__cross
    @property
    def zero_line(self):
        return self.__zero_line
    @property
    def cross_line(self):
        return self.__cross_line
    @property
    def draw(self):
        return self.__draw

SYMB = SymbolEnum()


class Game:
    def __init__(self):
        self.results = []
        self.active_symbol = SYMB.zero
        self.current_state = SYMB.unfinished
        self.initialize()

    def initialize(self):
        self.results = [str(i+1) for i in range(9)]
        self.active_symbol = SYMB.zero
        self.current_state = SYMB.unfinished

    def check_winner(self):
        """returns
            SYMB.unfinished, if game isn't finished
            SYMB.draw, if game ended in a draw
            SYMB.zero, if zero-player won
            SYMB.cross, if cross-player won """
        res = self.results
        line_list = []
        for i in range(3):
            line_list.append(res[i] + res[i + 3] + res[i + 6])
        for i in range(0, 7, 3):
            line_list.append(res[i] + res[i + 1] + res[i + 2])
        line_list.append(res[0] + res[4] + res[8])
        line_list.append(res[2] + res[4] + res[6])

        if any(line == SYMB.cross_line for line in line_list):
            return SYMB.cross
        if any(line == SYMB.zero_line for line in line_list):
            return SYMB.zero
        if all(line.find(SYMB.cross) != -1 and line.find(SYMB.zero) != -1 for line in line_list):
            return SYMB.draw
        return SYMB.unfinished

    def fill_cell(self, cell, state):
        """returns false, if move isn't made,
                   true, if move is made
                   state contains information in format ['some_information']"""
        if not isinstance(state, list):
            raise ValueError("state type must be list")
            #return False
        state.clear()
        try:
            cell = int(cell)
        except ValueError:
            state.append("cell number must be integer")
            return False
        if all(not (cell is item) for item in range(1, 10)):
            state.append("cell number must be integer from 1 to 9")
            return False
        cell -= 1
        if self.results[cell] == SYMB.zero or self.results[cell] == SYMB.cross:
            state.append('cell has already been filled')
            return False
        if self.current_state != SYMB.unfinished:
            state.append('game has already been finished')
            return False

        self.active_symbol = SYMB.cross if self.active_symbol == SYMB.zero else SYMB.zero
        self.results[cell] = self.active_symbol
        self.current_state = self.check_winner()
        state.append(self.current_state)
        return True

    def get_board(self):
        return '{}|{}|{}\n-----\n{}|{}|{}\n-----\n{}|{}|{}\n'.format(*self.results)


class GameInterface:
    def __init__(self):
        self.player1 = ''
        self.player2 = ''
        self.game = Game()

    def run(self):
        self.set_players()

        while True:
            self.play_game()
            while True:
                inp = input('try again with the same names? [y,n]\n')
                if inp == 'y':
                    break
                if inp == 'n':
                    self.set_players()
                    break
                print('write y or n\n')

    def play_game(self):
        self.game.initialize()
        result = ['init']

        while result[0] != SYMB.zero and result[0] != SYMB.cross and result[0] != SYMB.draw:
            print(self.game.get_board())
            cell_num = input()
            move = self.game.fill_cell(cell_num, result)
            if move is False:
                print(result[0])

        print(self.game.get_board())
        if result[0] == SYMB.cross:
            print(self.player1 + ' won!\n')
        elif result[0] == SYMB.zero:
            print(self.player2 + ' won!\n')
        else:
            print('Nobody won\n')


    def set_players(self):
        while True:
            inp = input('Player 1:')
            if inp.strip() == '':
                print('empty name, try again\n')
            else:
                self.player1 = inp
                break
        while True:
            inp = input('Player 2:')
            if inp.strip() == '':
                print('empty name, try again\n')
            else:
                self.player2 = inp
                break

if __name__ == "__main__":
    G = GameInterface()
    G.run()
