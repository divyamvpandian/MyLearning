result=[]

def findTriplets(arr):
    n=len(arr)
    i = 0

    for i in range(n-1):
        s = set()
        j=i+1
        for j in range(i+1,n):
            sum = -(arr[i]+arr[j])
            if sum in s:
                print(sum,arr[i],arr[j])
            else:
                s.add(arr[j])
            j+=1

def generateCombinations(inp):
    if '?' in inp:
        s1 = inp.replace("?",'0',1)
        generateCombinations(s1)
        s2 = inp.replace("?",'1',1)
        generateCombinations(s2)
    else:
        result.append(inp)

def countStr(n, bCount, cCount):

    # Base cases
    if (bCount < 0 or cCount < 0):
        return 0
    if (n == 0) :
        return 1
    if (bCount == 0 and cCount == 0):
        return 1

    # Three cases, we choose, a or b or c
    # In all three cases n decreases by 1.
    res = countStr(n - 1, bCount, cCount)
    res += countStr(n - 1, bCount - 1, cCount)
    res += countStr(n - 1, bCount, cCount - 1)

    return res


def main():
    print("https://www.geeksforgeeks.org/Google-topics-interview-preparation/ Easy/Meduim/Hard")
    ##1 Find all triplets with zero sum
    arr= [0, -1, 2, -3, 1]
    findTriplets(arr)

    ##2 Generate all binary strings from given pattern
    inp = "1??0?101"
    generateCombinations(inp)
    print(result)

    ##3 Count of strings that can be formed using a, b and c under given constraints

    n = 3 # Total number of characters
    print(countStr(n, 1, 2))
if __name__=='__main__':
    main()