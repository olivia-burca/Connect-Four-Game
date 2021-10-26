from termcolor import colored
import random


class Disc:
    '''
    Entity that represents a disc of a specified color
    '''

    def __init__(self, color):
        self._color = color

    def __str__(self):
        return colored('●', str(self._color))


class Board:
    '''
    The board entity
    '''

    def __init__(self):
        self._rows = 6
        self._columns = 7
        self._data = [[None for j in range(self._columns)] for i in range(self._rows)]

    @property
    def data(self):
        return self._data

    def __str__(self):
        '''
        :return: The string representation of the board
        '''

        board = '   1   2   3   4   5   6   7   \n'
        board += '-----------------------------\n'
        for i in range(6):
            for j in range(7):
                board += ' | '
                if self._data[i][j] is None:
                    board += '●'
                else:
                    board += str(self._data[i][j])
            board += ' | \n'
            board += '-----------------------------\n'
        return board

    def move(self, col, disc):
        '''
        Function that represents a move on the board
        :param col: the column in which the disc will be placed
        :param disc: the disc
        :return: False if the move is not valid
        '''
        if self._data[0][col - 1] is not None:
            return False

        for row in range(5):
            if self._data[row + 1][col - 1] is not None:
                self._data[row][col - 1] = disc
                break
            if self._data[row + 1][col - 1] is None and row == 4:
                self._data[row + 1][col - 1] = disc
                break

    def draw(self):
        """
        Checks if the game is a draw
        Returns True if the game is a draw and False otherwise
        """
        for i in range(6):
            for j in range(7):
                if self._data[i][j] is None:
                    return False

        return True

    def game_won(self):
        """
        Checks if the game was won be someone or the computer
        Returns True if the game was won, False otherwise
        """

        for i in range(6):
            for j in range(4):
                if self._data[i][j] is not None:
                    if self._data[i][j] == self._data[i][j + 1]:
                        if self._data[i][j] == self._data[i][j + 2]:
                            if self._data[i][j] == self._data[i][j + 3]:
                                return True

        for i in range(7):
            for j in range(3):
                if self._data[j][i] is not None:
                    if self._data[j][i] == self._data[j + 1][i]:
                        if self._data[j][i] == self._data[j + 2][i]:
                            if self._data[j][i] == self._data[j + 3][i]:
                                return True

        for i in range(3):
            for j in range(4):
                if self._data[i][j] is not None:
                    if self._data[i][j] == self._data[i + 1][j + 1]:
                        if self._data[i][j] == self._data[i + 2][j + 2]:
                            if self._data[i][j] == self._data[i + 3][j + 3]:
                                return True

        for i in range(3):
            j = 6
            while j > 2:
                if self._data[i][j] is not None:
                    if self._data[i][j] == self._data[i + 1][j - 1]:
                        if self._data[i][j] == self._data[i + 2][j - 2]:
                            if self._data[i][j] == self._data[i + 3][j - 3]:
                                return True
                j -= 1

        return False

    def is_win_possible(self):
        '''
        Checks if a win is possible with only one move, in order to either block the human from winning, or for the computer
        to win the game.

        :return: the column in which a disc needs to be placed if a win is possible, or False otherwise
        '''
        for i in range(6):
            for j in range(4):
                nr = 0
                d = None
                col = None
                for k in range(4):
                    if self._data[i][j + k] is not None:
                        if d is None:
                            d = self._data[i][j + k]
                            nr = 1
                        elif self._data[i][j + k] != d:
                            break
                        else:
                            nr += 1
                    else:
                        col = j + k

                if nr == 3 and col is not None:
                    if i == 5:
                        return col
                    elif self._data[i + 1][col] is not None:
                        return col

        for j in range(7):
            for i in range(3):
                if self._data[i + 3][j] is not None:
                    if self._data[i + 2][j] == self._data[i + 3][j]:
                        if self._data[i + 1][j] == self._data[i + 3][j]:
                            if self._data[i][j] is None:
                                return j

        for i in range(3):
            for j in range(4):
                nr = 0
                d = None
                col = None
                for k in range(4):
                    if self._data[i + k][j + k] is not None:
                        if d is None:
                            d = self._data[i + k][j + k]
                            nr = 1
                        elif self._data[i + k][j + k] != d:
                            break
                        else:
                            nr += 1
                    else:
                        col = j + k
                        k2 = k
                if nr == 3 and col is not None:
                    if i + k2 == 5:
                        return col
                    elif self._data[i + k2 + 1][col] is not None:
                        return col

        for i in range(3):
            j = 6
            while j > 2:
                nr = 0
                d = None
                col = None
                for k in range(4):
                    if self._data[i + k][j - k] is not None:
                        if d is None:
                            d = self._data[i + k][j - k]
                            nr = 1
                        elif self._data[i + k][j - k] != d:
                            break
                        else:
                            nr += 1
                    else:
                        col = j - k
                        k2 = k
                if nr == 3 and col is not None:
                    if i + k2 == 5:
                        return col
                    elif self._data[i + k2 + 1][col] is not None:
                        return col

                j -= 1

        return False


class Strategy:
    """
    Class decides computer's next move

    """

    def next_move(self, board, disc):
        """
        Return the computer's next move
        """
        raise Exception('Subclass strategy in order to implement computer play!')


class MoveStrategy(Strategy):
    '''
    The computer's strategy
    If the human can win from the next move, it blocks it
    If the computer can win from the next move, it does so
    If neither of this cases apply, it makes a random, but valid move.

    '''

    def next_move(self, board, disc):
        if board.is_win_possible() is not False:
            col = board.is_win_possible() + 1
            return col

        available_moves = []

        for col in range(7):
            if board._data[0][col] is None:
                available_moves.append(col)

        c = random.choice(available_moves)
        return c + 1


class Player:
    '''
    Entity to represent the human player
    '''

    def __init__(self, name, disc):
        self._name = name
        self._disc = disc

    @property
    def disc(self):
        return self._disc

    @property
    def name(self):
        return self._name

    def __str__(self):
        return self._name + " is playing with discs of this color: " + str(self._disc)
