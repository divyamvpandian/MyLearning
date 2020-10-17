import math


def main():
    t = int(input())
    while (t > 0):
        strin = input()
        a = strin.split(" ")[0]
        b = strin.split(" ")[1]
        p = strin.split(" ")[2]
        x = strin.split(" ")[3]
        result = ifcrct(int(a), int(b), int(p), int(x))
        print(result)
        t -= 1


def ifcrct(a, b, p, x):
    cnt = 0
    for i in range(1, x + 1):
        lhs = i * math.pow(a, i)
        rhs = b%p
        if (lhs == rhs):
            cnt += 1
    return cnt


if __name__ == '__main__':
    main()
