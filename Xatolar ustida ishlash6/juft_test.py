import unittest

from juft import juftmi

class JuftTop(unittest.TestCase):
    def test_juft(self):
        natija = juftmi(5)
        self.assertEqual(natija,"Juft")
        
unittest.main()

