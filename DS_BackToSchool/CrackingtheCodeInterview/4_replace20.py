import unittest

def replace20(str,length):
    newidx=len(str)
    for i in reversed(range(length)):
        if str[i] ==" ":
            str[newidx-3:newidx]='%20'
            newidx-=3
        else:
            str[newidx-1]=str[i]
            newidx-=1
    return str



class Test(unittest.TestCase):

    def testreplace(self):
        str1=list('abc   def   efd')
        str2=list('abc%20%20%20def%20%20%20efd')
        actual = replace20(str1,len(str2))
        print(actual,str2)
        self.assertEqual(actual,str2)

if __name__=='__main__':
    unittest.main()