import os,operator

def main():
    # input=['ggg','fff','aaa']
    # printSortedarr(input)
    sq = raise_to(2)
    print(sq.__closure__)
    print(sq(5))


def printSortedarr(input):
    def getlastLetter(str):
        return str[-1]
    output = sorted(input,key=getlastLetter)
    print(output)

def raise_to(e):
    def raise_to_exp(x):
        return pow(x,e)
    return raise_to_exp

if __name__=='__main__':
    main()

