import os


def main():
    vector= [1,1,2,2,2,2,2,3]
    n=2
    print(getfrequency(vector,n))


def getfrequency(vector,n):
    low=0
    high = len(vector)
    print(low,high)
    first = getFirst(vector,n,low,high)
    last = getLast(vector,n,low,high)
    print(first,last)
    return last-first+1

def getFirst(vector,n,low,high):
    mid = (low + high)  // 2
    if low <= high:
        if mid == 0  or (vector[mid]==n and n > vector[mid-1]):
            return mid
        elif vector[mid]<n:
            return getFirst(vector,n,mid+1,high)
        else:
            return getFirst(vector,n,low,mid-1)
    return -1

def getLast(vector,n,low,high):
    mid = (low + high)  //2
    if low <= high:
        if mid==n-1  or (vector[mid]==n and n < vector[mid+1]):
            return mid
        elif n < vector[mid]:
            return getLast(vector,n,low,mid-1)
        else:
            return getLast(vector,n,mid+1,high)

    return -1

if __name__=='__main__':
    main()

