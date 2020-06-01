import unittest
from dokumentarij import DokumentarijContoller

class DokumentarijUnittest (unittest.TestCase):

    def test_same_name(self):
        game_test=DokumentarijContoller()
        name1= game_test.get_new_name()
        name2= game_test.get_new_name() 
        self.assertNotEqual(str(name1), str(name2), "Moraju bit različita imena")

    

if __name__ == "__main__":
    unittest.main()
    
