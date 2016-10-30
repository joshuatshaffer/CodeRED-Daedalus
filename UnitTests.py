#!/usr/bin/env python2.7

from BuildPlanner import *

import unittest

class UnitTest (unittest.TestCase):
    def test_invalid_blocks (self):
        floating = [Block(0,0,1)]
        self.assertEqual(list_invalid_blocks(floating, 2, 2), floating)
        onGround = [Block(0,1,0)]
        self.assertEqual(list_invalid_blocks(onGround, 2, 2), [])
        sittingOnFloating = [Block(0,0,1), Block(0,0,2)]
        self.assertEqual(list_invalid_blocks(sittingOnFloating, 2, 2), sittingOnFloating)

if __name__ == '__main__':
    unittest.main()
