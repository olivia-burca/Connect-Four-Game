from entities import MoveStrategy, Player, Board, Disc


class UI:

    def checkInput(self, col):
        if col.isdigit():
            column = int(col)
            if column > 0 and column < 8:
                return True
        return False

    def read_human_move(self, player):
        col = input(str(player.name) + ', choose a column: ')

        return col

    def start_game(self):
        d1 = Disc('red')
        d2 = Disc('blue')
        board = Board()
        name = input('Type your name: ')
        human = Player(name,d1)
        strategy = MoveStrategy()
        print(human)
        print('The computer is playing with discs of this color: '+str(d2)+'\n')
        print(str(board))

        while(board.draw() is False):
            col = self.read_human_move(human)
            while self.checkInput(col) is False:
                print('Choose a number between 1 and 7!')
                col = self.read_human_move(human)

            while board.move(int(col),d1) == False:
                print('Cannot place disc here, column is full!')
                col = self.read_human_move(human)
                while self.checkInput(col) is False:
                    print('Choose a number between 1 and 7!')
                    col = self.read_human_move(human)

            print(board)
            if board.game_won() is True:
                print(human.name + ' wins!!')
                break
            print('It is the computer`s turn.')
            col2 = strategy.next_move(board,d2)
            print('The computer chose column ' + str(col2))
            board.move(col2,d2)
            print(board)
            if board.game_won() is True:
                print('The computer beat you :( ')
                break

        if board.draw() is True:
            print('It is a draw! ')





ui = UI()
ui.start_game()


