#! /usr/bin/env python

import unittest
import tick_tack

class TestGame(unittest.TestCase):

    def test_win(self):
        game = tick_tack.Game()
        res = []

        game.initialize()
        game.fill_cell(1, res)
        self.assertEqual(res[0], tick_tack.SYMB.unfinished)
        game.fill_cell(4, res)
        self.assertEqual(res[0], tick_tack.SYMB.unfinished)
        game.fill_cell(2, res)
        self.assertEqual(res[0], tick_tack.SYMB.unfinished)
        game.fill_cell(5, res)
        self.assertEqual(res[0], tick_tack.SYMB.unfinished)
        game.fill_cell(3, res)
        self.assertEqual(res[0], tick_tack.SYMB.cross)

        game.initialize()
        game.fill_cell(1, res)
        self.assertEqual(res[0], tick_tack.SYMB.unfinished)
        game.fill_cell(3, res)
        self.assertEqual(res[0], tick_tack.SYMB.unfinished)
        game.fill_cell(4, res)
        self.assertEqual(res[0], tick_tack.SYMB.unfinished)
        game.fill_cell(6, res)
        self.assertEqual(res[0], tick_tack.SYMB.unfinished)
        game.fill_cell(7, res)
        self.assertEqual(res[0], tick_tack.SYMB.cross)

        game.initialize()
        game.fill_cell(7, res)
        self.assertEqual(res[0], tick_tack.SYMB.unfinished)
        game.fill_cell(9, res)
        self.assertEqual(res[0], tick_tack.SYMB.unfinished)
        game.fill_cell(8, res)
        self.assertEqual(res[0], tick_tack.SYMB.unfinished)
        game.fill_cell(6, res)
        self.assertEqual(res[0], tick_tack.SYMB.unfinished)
        game.fill_cell(5, res)
        self.assertEqual(res[0], tick_tack.SYMB.unfinished)
        game.fill_cell(3, res)
        self.assertEqual(res[0], tick_tack.SYMB.zero)

    def test_draw(self):
        game = tick_tack.Game()
        game.initialize()
        res = []
        game.fill_cell(1, res)
        self.assertEqual(res[0], tick_tack.SYMB.unfinished)
        game.fill_cell(2, res)
        self.assertEqual(res[0], tick_tack.SYMB.unfinished)
        game.fill_cell(5, res)
        self.assertEqual(res[0], tick_tack.SYMB.unfinished)
        game.fill_cell(9, res)
        self.assertEqual(res[0], tick_tack.SYMB.unfinished)
        game.fill_cell(6, res)
        self.assertEqual(res[0], tick_tack.SYMB.unfinished)
        game.fill_cell(4, res)
        self.assertEqual(res[0], tick_tack.SYMB.unfinished)
        game.fill_cell(3, res)
        self.assertEqual(res[0], tick_tack.SYMB.unfinished)
        game.fill_cell(7, res)
        self.assertEqual(res[0], tick_tack.SYMB.unfinished)
        game.fill_cell(8, res)
        self.assertEqual(res[0], tick_tack.SYMB.draw)

    def test_board(self):
        game = tick_tack.Game()
        game.initialize()
        res = []
        game.fill_cell(1, res)
        game.fill_cell(5, res)
        game.fill_cell(9, res)
        self.assertEqual(game.get_board(), "X|2|3\n-----\n4|O|6\n-----\n7|8|X\n")

    def test_wrong_input(self):
        game = tick_tack.Game()
        game.initialize()
        res = []
        self.assertTrue(game.fill_cell('1', res))
        self.assertTrue(game.fill_cell('2', res))
        self.assertTrue(game.fill_cell('3', res))
        self.assertFalse(game.fill_cell('3', res))
        self.assertFalse(game.fill_cell('-1', res))
        self.assertFalse(game.fill_cell('10', res))
        self.assertFalse(game.fill_cell('qwe', res))
        self.assertFalse(game.fill_cell('', res))
        self.assertFalse(game.fill_cell(' ', res))
        self.assertFalse(game.fill_cell('2.5', res))
        res = 0
        self.assertRaises(ValueError, game.fill_cell, '2', res)
        res = 'srtr'
        self.assertRaises(ValueError, game.fill_cell, '2', res)
        res = (1, 2, 3)
        self.assertRaises(ValueError, game.fill_cell, '2', res)
        res = {'qwe': 'qwe'}
        self.assertRaises(ValueError, game.fill_cell, '2', res)

if __name__ == '__main__':
    unittest.main()
