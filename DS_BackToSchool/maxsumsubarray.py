

def maxsubarraykadane(arr):
    maxsum=0
    sum=0
    i=0
    while i<len(arr)-1:
        if sum+arr[i]>0:
            sum+=arr[i]
        else:
            sum=0
        maxsum=max(maxsum,sum)
        i+=1
    return maxsum

def maxsubArryDC(arr,low,high):
    if low==high:
        return arr[low]
    mid = (low+high)//2
    i=mid
    rightmax=leftmax=0
    sum=0

    while i>=low:
        sum+=arr[i]
        i-=1
        leftmax=max(sum,leftmax)
    j=mid+1
    sum=0
    while j<=high:
        sum+=arr[j]
        j+=1
        rightmax=max(sum,rightmax)
    middlehigh = leftmax + rightmax
    left = maxsubArryDC(arr,low,mid)
    right = maxsubArryDC(arr,mid+1,high)

    return max(middlehigh,left,right)



def maxsubArry(arr,n):
    res = -3423423

    # while subarraysize<=n:
    #     startidx=0
    #     while startidx<n:
    #         if startidx+subarraysize>n:
    #             break
    #         sum=0
    #         i=startidx
    #         while i < startidx+subarraysize:
    #             sum+=arr[i]
    #             i+=1
    #         res = max(sum,res)
    #         startidx+=1
    #     subarraysize+=1
    startidx=0
    while startidx<n:
        sum=0
        subarraysize=1
        while subarraysize<=n:
            if startidx+subarraysize>n:
                break
            sum+=arr[startidx+subarraysize-1]
            res = max(sum,res)
            subarraysize+=1
        startidx+=1
    return res


def main():
    arr=[ 2, -4, 1, 9, -6, 7, -3 ]

    n=len(arr)
    print("The maximmum sum of subarray for the given input via iterative method is " , maxsubArry(arr,n))
    print("The maximmum sum of subarray for the given input via divide Conquer method is " , maxsubArryDC(arr,0,n-1))
    print("The maximmum sum of subarray for the given input via kadane Algo is " , maxsubarraykadane(arr))

if __name__ == '__main__':
    main()

