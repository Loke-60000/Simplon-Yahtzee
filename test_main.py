import unittest
from unittest.mock import patch
from main import dices

class TestDices(unittest.TestCase):

    @patch('builtins.input', side_effect=['2', ' ', ' ', ' ', '1', ' ', ' '])  
    @patch('random.randint', return_value=3) 
    def test_dices_without_human_input(self, mock_randint, mock_input):
        try:
            dices()
            print('Test OK') 
        except Exception as e:
            self.fail(f"Test failed due to an unexpected error: {e}")

if __name__ == '__main__':
    unittest.main()
