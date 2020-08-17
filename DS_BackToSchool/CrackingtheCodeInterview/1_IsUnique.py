import unittest, os

def isUniq(str):
    if(len(str)>128):
        return False

    charset=[False for i in range(128)]
    for char in str:
        val = ord(char)
        if charset[val]:
            return False
        charset[val] = True
    return True


class Test(unittest.TestCase):
    strT={"abs","fedw"," "}
    strF={"grgr","hb 627jh=j ()"}

    def test_unique(self):
        #true
        for s in self.strT:
            actual=isUniq(s)
            print(s,actual)
            self.assertTrue(actual)

        for s in self.strF:
            actual=isUniq(s)
            print(s,actual)
            self.assertFalse(actual)


if __name__=='__main__':
    unittest.main()

