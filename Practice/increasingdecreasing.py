def main():
    arr = [1 ,1,1,1,1]
    print(arr, " is ", isMonotonic(arr))
    arr = [1 ,2,5,5,7]
    print(arr, " is ", isMonotonic(arr))
    arr = [4,6,7,3]
    print(arr, " is ", isMonotonic(arr))
    arr = [9,4,4,2,2,1]
    print(arr, " is ", isMonotonic(arr))
    arr = [1 ,2,3,4,5,6]
    print(arr, " is ", isMonotonic(arr))
    arr = [9,9,6,5,4,3,1,1,1]
    print(arr, " is ", isMonotonic(arr))
    arr = [9,9,6,5,4,3,1,1,1,-9]
    print(arr, " is ", isMonotonic(arr))

def isMonotonic(arr):
    type=None
    if arr[0] < arr[1]:
        type = "inc"
    elif arr[0] > arr[1]:
        type = "dec"
    else:
        prev = arr[1]
        for i in range(2, len(arr)):
            if prev < arr[i]:
                type = "inc"
                break
            elif prev > arr[i]:
                type = "dec"
                break
            else:
                prev = arr[i]
    if type is None:
        return True
    prev = arr[1]
    for i in range(2, len(arr)):
        if type=="inc":
            if prev > arr[i]:
                return False
        if type=="dec":
            if prev < arr[i]:
                return False
        prev=arr[i]
    return True


if __name__ == '__main__':
    main()
