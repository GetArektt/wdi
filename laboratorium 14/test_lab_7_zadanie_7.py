import lab_7_zadanie_7
import unittest
#import pytest

class TestSilnia(unittest.TestCase):

    def test_przedzial(self):
        M=lab_7_zadanie_7.wczytywanie()
        self.assertGreaterEqual(M,1)
        self.assertLess(M,10000)
    def test_wartosc(self):
        M=lab_7_zadanie_7.wczytywanie()
        self.assertRaises(ValueError, M, "a")
        self.assertRaises(ValueError, M, 3+5j)
        self.assertRaises(ValueError, M, True)

class TestSilnia_P:

    def test_przedzial_P(self):
        M=500
        assert M >= 1
        assert M < 10000
