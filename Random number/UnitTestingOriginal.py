#_*_Coding:utf-8_*_
import unittest
from OriginalUnitTesting import compare

class TestRandom(unittest.TestCase):
    def test_guess1(self):         #testing quit
        s=compare()
        self.assertEqual(s,0)
    def test_guess2(self):         #testing less
        s = compare()
        self.assertEqual(s, 1)
    def test_guess3(self):          #testing greater
        s = compare()
        self.assertEqual(s, 2)
    def test_guess4(self):          # testing same
        s = compare()
        self.assertEqual(s, 3)



if __name__ == '__main__':
    unittest.main()