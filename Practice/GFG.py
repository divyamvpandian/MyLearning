import time
# code
import math


def main():
    # removeDupsOnly("geeks for geeks")
    # print(isanagram("tvc","act"))
    # t = int(input())
    # while(t>0):
    #     strin = input()
    #     n = strin.split(" ")[0]
    #     givensum = strin.split(" ")[1]
    #     arrinput = input()
    #     arr = [int(x) for x in arrinput.split(" ")]
    #     start,end=getsubarray(arr,int(n),int(givensum))
    #     print(start,end)
    #     t-=1
    # inp = [1,3,2,5]
    # inp.sort()
    # print(counttriplets(inp))
    # mergeArrays()
    # print(add_one([1,2,3,4]))
    # print(add_one([9,9,7,7]))
    # print(add_one([4,9,9,9]))
    # print(add_one([9,9,9,9]))
    # t = int(input())
    # while(t>0):
    #     strin = input()t
    #     result=reversestr(strin)
    #     print(result)
    #     t-=1
    # generatewords("","ABSG")
    permUtil("NNCA")
    # nextLargerelementstl([1,3,2,4])
    # nextLargerelementstl([4,3,2,1])
    # nextLargerelementstl([1,4,5,7,3,0])
    # nextLargerelement([1,3,2,4])
    # nextLargerelement([4,3,2,1])
    # nextLargerelement([1,4,5,7,3,0])
    # t = int(input())
    # while(t>0):
    #     n = int(input())
    #     strin = input()
    #     arr=strin.split()
    #     nextLargerelement(arr)
    #     t-=1
    # print(removeDups("accdd"))
    # print(removeDups("accdde"))
    # print(removeDups("geeksforgeek"))
    # print(removeDups("acaaabbbacdddd"))
    # print(rotatedtwice("amazon","azknam"))
    # t = int(input())
    # while(t>0):
    #     strin = str(input())
    #     print(getlongestpalindrome(strin))
    #     t-=1
    # generatewords("","ADBSG")


def ispalnidrome(str):
    return str == str[::-1]


def isanagram(str1, str2):
    if len(str1) != len(str2):
        return False
    else:
        return sum(ord(ch) for ch in str1) == sum(ord(ch) for ch in str2)

    # def getlongestpalindrome(input):
    # if len(input)==1:
    #     return -1
    # if ispalnidrome(input):
    #     return input
    # else:
    #     lstr = getlongestpalindrome(input[1:])
    #     if lstr!="":
    #         return lstr
    #     else:
    #         rstr = getlongestpalindrome(input[:-1])
    #         if rstr!="":
    #             return rstr
    # return -1
    # while :
    #     if ispalnidrome(input):
    #         return input
    #     else:
    #         linput =input[1:]
    #         rinput =input[:-1]


def getsubarray(arr, n, givensum):
    minidx = 0
    sum = arr[minidx]
    for i in range(1, n):
        sum += arr[i]
        if sum == givensum:
            return minidx + 1, i + 1
        if sum > givensum:
            while (sum > givensum):
                sum -= arr[minidx]
                if sum == givensum:
                    return minidx + 2, i + 1
                minidx += 1


def counttriplets(arr):
    n = len(arr)
    counter = 0;
    i = 0;
    j = n - 2
    k = n - 1
    loops = 0
    while k > 1:
        print(loops)
        if j > i:
            if arr[i] + arr[j] < arr[k]:
                i += 1
            elif arr[i] + arr[j] > arr[k]:
                j -= 1
            else:
                counter += 1
                i += 1
                j -= 1
        else:
            k = k - 1;
            j = k - 1;
            i = 0;
        loops += 1
    if counter == 0:
        return -1
    else:
        return counter
    return 0


def add_one(arr):
    n = len(arr)
    output = [None] * n
    if (arr[n - 1]) != 9:
        arr[n - 1] = arr[n - 1] + 1
        return arr
    carry = 1
    output[n - 1] = 0
    for i in range(n - 2, -1, -1):
        res = arr[i] + carry
        carry = (res) // 10
        ans = (res) % 10
        output[i] = ans
    if carry == 1:
        list = [1]
        list.extend(output)
        return list
    return output


def generatewords(prefix, instr):
    n = len(instr)
    if n == 0:
        print(prefix)
    for i in range(0, n):
        generatewords(prefix + instr[i], instr[0:i] + instr[i + 1:n])


def mergeArrays():
    a1 = [1, 5, 9, 10, 15, 20]
    a2 = [2, 3, 8, 13]
    n1 = len(a1)
    n2 = len(a2)
    print(a1)
    print(a2)
    if a2[0] >= a1[n1 - 1]:
        return
    j = n2 - 1
    while j >= 0:
        for i in range(0, n1 - 1):
            if a1[i] > a2[j]:
                lastelement = a1[n1 - 1]
                pos = n1 - 1
                while pos > i:
                    a1[pos] = a1[pos - 1]
                    pos -= 1
                a1[pos] = a2[j]
                a2[j] = lastelement
                print(a1)
                print(a2)
        j -= 1


def reversestr(instr):
    words = []
    words = instr.split(".")
    words.reverse()
    outstr = ".".join([str(val) for val in words])
    return outstr


def permUtil(instr):
    strchar = []
    counts = []
    level = 0
    result = [None for i in range(0, len(instr))]
    strcounts = {}
    arr = instr[:]
    for c in arr:
        if c in strcounts.keys():
            strcounts[c] += 1
        else:
            strcounts[c] = 1

    for i in sorted(strcounts):
        strchar.append(i)
        counts.append(strcounts[i])
    perm(strchar, counts, level, result)


def perm(strch, counts, level, result):
    # exit condition
    if level == len(result):
        print("".join([i for i in result]))

    for i in range(0, len(strch)):
        if counts[i] == 0:
            continue
        result[level] = strch[i]
        counts[i] -= 1
        perm(strch, counts, level + 1, result)
        counts[i] += 1


def nextLargerelement(arr):
    res = []
    n = len(arr)
    if arr == sorted(arr, reverse=True):
        print("-1" * n)
        return
    for i in range(0, n - 1):
        found = False
        for j in range(i + 1, n):
            if arr[j] > arr[i]:
                found = True
                res.append(arr[j])
                break
        if not found:
            res.append(-1)
    res.append(-1)
    print(" ".join([str(i) for i in res]))


def nextLargerelementstl(arr):
    n = len(arr)
    if arr == sorted(arr, reverse=True):
        print("-1" * n)
        return
    stack = []
    res = [None] * n
    j = 0
    stack.append(arr[0])

    for i in range(1, n):
        while len(stack) > 0 and stack[-1] < arr[i]:
            res[j] = arr[i]
            j += 1
            stack.pop()
        stack.append(arr[i])
    while j < n:
        res[j] = -1
        j += 1
    print(" ".join([str(i) for i in res]))


def distinctElements(str):
    # mylist = []
    # mylist = [char for char in str]
    # mylist = list( dict.fromkeys(mylist) )
    # str = mylist = "".join([char for char in mylist])
    # print(str)
    #
    # remove only adjacent
    i = 1
    prevchar = ""
    dl = []
    j = len(str) - 1
    dl.append(str[0])
    while i <= j:
        # print(dl)
        char = str[i]
        if len(dl) > 0 and dl[-1] != char:
            dl.append(char)
            i += 1
        else:
            while (dl[-1] == char):
                if i < j:
                    i += 1
                    char = str[i]
                elif i == j:
                    i += 1
                    dl.pop()
                    break
            dl.pop()
    print(dl)


def removeDupsOnly(str):
    ll = []
    for i in range(0, len(str)):
        if str[i] not in ll:
            ll.append(str[i])
    #     if len(ll) == 0 or str[i] != ll[-1]:
    #         ll.append(str[i])
    print("".join([item for item in ll]))


def removeDups(str):
    n = len(str)
    if n == 1 or n == 0:
        return str
    if str[0] == str[1]:
        startpos = 2
        while startpos < n and str[0] == str[startpos]:
            startpos += 1
        return removeDups(str[startpos:n])
    else:
        return str[0] + removeDups(str[1:])


def rotatedtwice(str1, str2):
    if len(str1) != len(str2):
        return False
    n1 = len(str1)
    i = 0
    j = n1 - 2
    n2 = n1
    while i < n1 and j < n2:
        if str1[i] != str2[j]:
            return False
        else:
            if j == n2 - 1:
                j = 0
                n2 = n1 - 2
            else:
                j += 1
        i += 1
    return True


if __name__ == '__main__':
    main()
