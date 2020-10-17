import math

def main():
    t = int(input())
    while(t>0):
        strin = input()
        m = strin.split(" ")[0]
        n = strin.split(" ")[1]
        result=addmandn(int(m),int(n))
        print(result)
        t-=1

def countDigit(n):
    return math.floor(math.log(n, 10)+1)

def addmandn(m,n):
    x=m+n
    if(countDigit(x)==countDigit(n)):
        return n
    else:
        return x

    return 0
#
# def countSquares(b):
#     b = b-2
#     b= b/2
#     return b *(b-1)

if __name__ == '__main__':
    main()
