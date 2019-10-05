#! /usr/bin/env python

import tick_tack
import unittest

class TestGame(unittest.TestCase):

    def test_win(self):
        g = tick_tack.Game()
        res = []

        g.initialize()
        g.fill_cell(1, res)
        self.assertEqual(res[0], tick_tack.SYMB.unfinished)
        g.fill_cell(4, res)
        self.assertEqual(res[0], tick_tack.SYMB.unfinished)
        g.fill_cell(2, res)
        self.assertEqual(res[0], tick_tack.SYMB.unfinished)
        g.fill_cell(5, res)
        self.assertEqual(res[0], tick_tack.SYMB.unfinished)
        g.fill_cell(3, res)
        self.assertEqual(res[0], tick_tack.SYMB.cross)

        g.initialize()
        g.fill_cell(1, res)
        self.assertEqual(res[0], tick_tack.SYMB.unfinished)
        g.fill_cell(3, res)
        self.assertEqual(res[0], tick_tack.SYMB.unfinished)
        g.fill_cell(4, res)
        self.assertEqual(res[0], tick_tack.SYMB.unfinished)
        g.fill_cell(6, res)
        self.assertEqual(res[0], tick_tack.SYMB.unfinished)
        g.fill_cell(7, res)
        self.assertEqual(res[0], tick_tack.SYMB.cross)

        g.initialize()
        g.fill_cell(7, res)
        self.assertEqual(res[0], tick_tack.SYMB.unfinished)
        g.fill_cell(9, res)
        self.assertEqual(res[0], tick_tack.SYMB.unfinished)
        g.fill_cell(8, res)
        self.assertEqual(res[0], tick_tack.SYMB.unfinished)
        g.fill_cell(6, res)
        self.assertEqual(res[0], tick_tack.SYMB.unfinished)
        g.fill_cell(5, res)
        self.assertEqual(res[0], tick_tack.SYMB.unfinished)
        g.fill_cell(3, res)
        self.assertEqual(res[0], tick_tack.SYMB.zero)

    def test_draw(self):
        g = tick_tack.Game()
        g.initialize()
        res = []
        g.fill_cell(1, res)
        self.assertEqual(res[0], tick_tack.SYMB.unfinished)
        g.fill_cell(2, res)
        self.assertEqual(res[0], tick_tack.SYMB.unfinished)
        g.fill_cell(5, res)
        self.assertEqual(res[0], tick_tack.SYMB.unfinished)
        g.fill_cell(9, res)
        self.assertEqual(res[0], tick_tack.SYMB.unfinished)
        g.fill_cell(6, res)
        self.assertEqual(res[0], tick_tack.SYMB.unfinished)
        g.fill_cell(4, res)
        self.assertEqual(res[0], tick_tack.SYMB.unfinished)
        g.fill_cell(3, res)
        self.assertEqual(res[0], tick_tack.SYMB.unfinished)
        g.fill_cell(7, res)
        self.assertEqual(res[0], tick_tack.SYMB.unfinished)
        g.fill_cell(8, res)
        self.assertEqual(res[0], tick_tack.SYMB.draw)

    def test_board(self):
        g = tick_tack.Game()
        g.initialize()
        res = []
        g.fill_cell(1, res)
        g.fill_cell(5, res)
        g.fill_cell(9, res)
        self.assertEqual(g.get_board(), "X|2|3\n-----\n4|O|6\n-----\n7|8|X\n")

    def test_wrong_input(self):
        g = tick_tack.Game()
        g.initialize()
        res = []
        self.assertTrue(g.fill_cell('1', res))
        self.assertTrue(g.fill_cell('2', res))
        self.assertTrue(g.fill_cell('3', res))
        self.assertFalse(g.fill_cell('3', res))
        self.assertFalse(g.fill_cell('-1', res))
        self.assertFalse(g.fill_cell('10', res))
        self.assertFalse(g.fill_cell('qwe', res))
        self.assertFalse(g.fill_cell('', res))
        self.assertFalse(g.fill_cell(' ', res))
        self.assertFalse(g.fill_cell('2.5', res))
        res = 0
        self.assertRaises(ValueError, g.fill_cell, '2', res)
        res = 'srtr'
        self.assertRaises(ValueError, g.fill_cell, '2', res)
        res = (1,2,3)
        self.assertRaises(ValueError, g.fill_cell, '2', res)
        res = {'qwe': 'qwe'}
        self.assertRaises(ValueError, g.fill_cell, '2', res)


if __name__ == '__main__':
    unittest.main()
