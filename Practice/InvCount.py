def countInv(arr):
    # exit condition for recursion
    if len(arr)<=1:
        return 0
    mid = len(arr)//2
    leftarr=arr[:mid]
    rightarr=arr[mid:]
    lefinv = countInv(leftarr)
    rightinv = countInv(rightarr)
    i=0
    j=0
    k=0
    invcount=0
    while i<len(leftarr) and j<len(rightarr):
        if leftarr[i] <= rightarr[j]:
            arr[k]=leftarr[i]
            i+=1
            k+=1
        else:
            arr[k]=rightarr[j]
            j+=1
            k+=1
            invcount+=len(leftarr)-i
    while i<len(leftarr):
        arr[k]=leftarr[i]
        k+=1
        i+=1
    while j<len(rightarr):
        arr[k]=rightarr[j]
        k+=1
        j+=1
    totalcount= rightinv+lefinv+invcount
    return totalcount


# Driver Code
# Given array is
arr = [1, 20, 6, 4, 5]
n = len(arr)
result = countInv(arr)
print("Number of inversions are", result)
