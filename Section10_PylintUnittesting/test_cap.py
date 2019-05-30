'''
Unit testing example
'''

import unittest
import cap

class TestCap(unittest.TestCase):
    '''
    Unit test Asserts
    '''
    def test_one_word(self):
        '''
        One word test assert
        '''
        text = 'python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Python')

    def test_multiple_words(self):
        '''
        Multiple word test assert
        '''
        text = 'monty python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Monty Python')


if __name__ == '__main__':
    unittest.main()
