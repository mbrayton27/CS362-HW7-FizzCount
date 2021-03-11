import unittest
import main1

class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(main1.print_count(), '12Buzz4FizzBuzz78BuzzFizz11Buzz1314FizzBuzz1617Buzz19FizzBuzz2223BuzzFizz26Buzz2829FizzBuzz3132Buzz34FizzBuzz3738BuzzFizz41Buzz4344FizzBuzz4647Buzz49FizzBuzz5253BuzzFizz56Buzz5859FizzBuzz6162Buzz64FizzBuzz6768BuzzFizz71Buzz7374FizzBuzz7677Buzz79FizzBuzz8283BuzzFizz86Buzz8889FizzBuzz9192Buzz94FizzBuzz9798BuzzFizz')

if __name__ == '__main__':
    unittest.main()
