import unittest

from son import juft_mi

class SonTest(unittest.TestCase):
    def test_son1(self):
        #son1 = juft_mi(10)
        self.assertTrue(juft_mi(10),son1)
   
    def test_son2(self):
        son2 = juft_mi(3)
        self.assertFalse(son2)
        
unittest.main()



# import unittest

# from son import kvadrat_yuza, uchburchak_yuza, doira_yuza

# class MathTest(unittest.TestCase):
#     def test_kvadrat(self):
#         self.assertEqual(kvadrat_yuza(4), 16)

#     def test_uchburchak(self):
#         self.assertEqual(uchburchak_yuza(6, 4), 12)

#     def test_doira(self):
#         self.assertAlmostEqual(doira_yuza(10), 314.159)

# unittest.main()

    
        
