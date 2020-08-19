import unittest

def getreverse(str):
    return(str[::-1])



class Test(unittest.TestCase):

    def testrevStr(self):
        str="abcde"
        revstr="edcba"
        actual = getreverse(str)
        print(str,actual)
        self.assertEqual(actual,revstr)

if __name__ == '__main__':
    unittest.main()