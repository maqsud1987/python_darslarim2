import unittest

from qoshish import yigindi

class AdditionTest(unittest.TestCase):
    
    
    def test_qoshish_1(self):
        test1=yigindi(2, 3)
        self.assertEqual(test1, 5)
        
    def test_qoshish_2(self):
        test2=yigindi(10,20)
        self.assertEqual(test2,30)
        
    def test_qoshish_3(self):
        test3=yigindi(0,0)
        self.assertEqual(test3,0)
        
    def test_qoshish_4(self):
        test4=yigindi(0,-3)
        self.assertEqual(test4,-5)
        
    
        
unittest.main()   
