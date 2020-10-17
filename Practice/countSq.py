import math

def main():
    t = int(input())
    while(t>0):
        n = input()
        result=countSquares(int(n))
        print(result)
        t-=1

def countSquares(b):
    answer=0
    while b > 2:
        answer+=(b-2)//2
        b = b-2
    return answer

if __name__ == '__main__':
    main()
