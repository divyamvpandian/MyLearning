import cmath,math
from functools import reduce
import operator


def inductive(ohms):
    return complex(0.0,ohms)

def capacitive(ohms):
    return complex(0.0, -ohms)

def resistive(ohms):
    return complex(ohms)

def impedance(components):
    return sum(components)

def combine(size,colur,animal):
    return '{}  {}  {}'. format(size,colur,animal)

def testmap():
    size=[1,2,3]
    colur=["red","bluee","green"]
    animal=["bear","d0g","Cat"]
    # print(combine(size,colur,animal))
    print(list(map(combine,size,colur,animal)))

def testfilter():
    pos = filter(lambda x:x>0,[1,-6,2,23,-8])
    print(pos)
    for i in pos:
        print(i)


def mul(x,y):
    if x>0:
        print(x+y)
        return x+y
    else:
        print(x)
        return x

def testmul():
    reduce(mul,range(1,20))

def sign(x):
    return x>0 - x<0

# def orientation(p,q,r):
    # d=
    # return sign(d)
def main():
    # impedanceresult = impedance([inductive(10),resistive(10),capacitive(5)])
    # phase = cmath.phase(impedanceresult)
    # degrees = math.degrees(phase)
    # print(impedanceresult,phase,degrees)
    # testmap()
    # testfilter()
    testmul()


if __name__ == '__main__':
    main()

