import unittest

from entities import Disc, Board, Player, Strategy, MoveStrategy


class Tests(unittest.TestCase):

    def test_board(self):
        d1 = Disc('red')
        d2 = Disc('blue')
        b = Board()
        b.data[0][1] = d2
        b.data[1][1] = d2
        b.data[2][1] = d2
        b.data[3][1] = d1
        b.data[4][1] = d1
        b.data[5][1] = d1
        b.data[5][0] = d1
        self.assertEqual(len(str(b)),497)
        self.assertEqual(b.move(2,d1), False)
        b.move(7,d2)
        b.move(7,d2)
        self.assertEqual(b.data[5][6],d2)
        self.assertEqual(b.data[4][6], d2)
        self.assertEqual(b.game_won(),False)
        self.assertEqual(b.draw(),False)
        self.assertEqual(b.is_win_possible(),False)
        b.data[5][2] = d1
        self.assertEqual(b.is_win_possible(),3)
        b.move(4,d1)
        self.assertEqual(b.game_won(),True)

    def test_player(self):
        d = Disc('red')
        p = Player('Ana',d)
        self.assertEqual(p.name,'Ana')
        self.assertEqual(p.disc,d)
        self.assertEqual(len(str(p)),51)


    def test_strategy(self):
        b = Board()
        d1 = Disc('red')
        d2 = Disc('blue')
        s = Strategy()
        ms = MoveStrategy()
        b.data[0][1] = d2
        b.data[1][1] = d2
        b.data[2][1] = d2
        b.data[3][1] = d1
        b.data[4][1] = d1
        b.data[5][1] = d1
        b.data[5][0] = d1
        self.assertIn(ms.next_move(b,d1),[1,2,3,4,5,6,7])
        b.data[5][2] = d1
        self.assertEqual(ms.next_move(b,d1),4)

