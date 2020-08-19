import unittest
from collections import Counter

def isPermuation(str1,str2):
    if len(str1)!=len(str2):
        return False
    # return sort(str1)==sort(str2)
    counter = Counter()
    for c in str1:
        counter[c]+=1
    for c in str2:
        if counter[c]==0:
            return False
        counter[c]-=1
    return True


def sort(str):
    sortedstr = sorted(str)
    return  sortedstr


class Test(unittest.TestCase):

    truecases = {('abc','bac'),('edf','fed')}
    falsecases = {('fred','reda'),('cdes','swqa'),('eda','asede')}
    def test_isPermutation(self):
        for cases in self.truecases:
            str1=cases[0]
            str2=cases[1]
            actual = isPermuation(str1,str2)
            print(cases,actual)
            self.assertTrue(actual)
        for cases in self.falsecases:
            str1=cases[0]
            str2=cases[1]
            actual = isPermuation(str1,str2)
            print(cases,actual)
            self.assertFalse(actual)



if __name__=='__main__':
    unittest.main()