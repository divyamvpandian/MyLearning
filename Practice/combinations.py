import sys
def printCombination(arr, n, r):

    # A temporary array to store
    # all combination one by one
    data = [0] * r

    # Print all combination using
    # temprary array 'data[]'
    combinationUtil(arr, n, r, 0, data, 0)

def combinationUtil(arr, n, r, index, data, i):

    # Current cobination is ready,
    # print it
    if (index == r):
        for j in range(r):
            print(data[j], end = " ")
        print()
        return

    # When no more elements are
    # there to put in data[]
    if (i >= n):
        return

    # current is included, put
    # next at next location
    data[index] = arr[i]
    combinationUtil(arr, n, r, index + 1,
                    data, i + 1)

    # current is excluded, replace it
    # with next (Note that i+1 is passed,
    # but index is not changed)
    combinationUtil(arr, n, r, index,
                    data, i + 1)


def main():
    arr=[ 1,2,3,4,5 ]
    n=len(arr)
    r=3
    while r<=3:
        printCombination(arr, n, r)
        r-=1

if __name__ == '__main__':
    main()

