import unittest

# 1 🔵 Yuzani tekshirish

from doira import yuza

class YuzaTest(unittest.TestCase):
    def test_yuza(self):
        test1 = yuza(10)
        self.assertAlmostEqual(test1, 314.159)
        
unittest.main()

# 2 🔴  Peremetrni tekshirish

from doira import peremetr

class PeremetrTest(unittest.TestCase):
    def test_peremetr(self):
        test2 = peremetr(10)
        self.assertAlmostEqual(test2, 62.8318)
        
unittest.main()
        
        
