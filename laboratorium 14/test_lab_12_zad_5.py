import lab_12_zad_5
import unittest
#import pytest

class TestDzialania(unittest.TestCase):

    def test_dodawanie(self):
        a=(5,3)
        b=(3,8)
        c= lab_12_zad_5.dodawanie(a,b)
        self.assertEqual(c, (8,11))


    def test_odejmowanie(self):
        a=(6,9)
        b=(4,2)
        c= lab_12_zad_5.odejmowanie(a,b)
        self.assertEqual(c, (2,7))

    def test_mnozenie(self):
        a=(5,5)
        b=(-4,142)
        c= lab_12_zad_5.mnozenie(a,b)
        self.assertEqual(c, (-730,690))

    def test_dzielenie(self):
        a = (14,0)
        b= (2,0)
        c=lab_12_zad_5.dzielenie(a,b)
        self.assertNotEqual(c[1], 0)



class TestDzialania_P:

    def test_dodawanie(self):
        a=(5,3)
        b=(3,8)
        c= lab_12_zad_5.dodawanie(a,b)
        assert c == (8,11)


    def test_odejmowanie(self):
        a=(6,9)
        b=(4,2)
        c= lab_12_zad_5.odejmowanie(a,b)
        assert c == (2,7)

    def test_mnozenie(self):
        a=(5,5)
        b=(-4,142)
        c= lab_12_zad_5.mnozenie(a,b)
        assert c == (-730,690)


    def test_dzielenie(self):
        a = (14,0)
        b= (2,0)
        c=lab_12_zad_5.dzielenie(a,b)
        assert c != 0

