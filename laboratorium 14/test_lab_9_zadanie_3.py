from lab_9_zadanie_3 import wyznacznik,jednostka
import unittest
#import pytest


class TestWyznacznik(unittest.TestCase):

    def test_wyznacznik(self):
        wartosc=wyznacznik([[1,5,1],[7,7,3],[3,2,5]], wynik=0)
        wartosc2=wyznacznik([[3,-1,1],[5,1,4],[-1,3,2]], wynik=0)
        self.assertEqual(wartosc, -108)
        self.assertEqual(wartosc2, 0)

class TestJednostka(unittest.TestCase):

    def test_macierz_jednostkowa(self):
        wymiar=3
        self.assertIs(jednostka(wymiar),[[1, 0, 0], [0, 1, 0], [0, 0, 1]])

#PYTEST

class TestWyznacznik_P:

    def test_wyznacznik_P(self):
        wartosc = wyznacznik([[1, 5, 1], [7, 7, 3], [3, 2, 5]], wynik=0)
        wartosc2 = wyznacznik([[3, -1, 1], [5, 1, 4], [-1, 3, 2]], wynik=0)
        assert wartosc == -108
        assert wartosc2 == 0
