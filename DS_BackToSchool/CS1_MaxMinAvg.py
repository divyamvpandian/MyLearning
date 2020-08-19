import sys
# CS1
##1_PrefixAverage
def callAll():
    inp=[2,4,9,6,7]
    ## Smoothing Fn
    i=0
    sum=0
    out=[]
    for val in inp:
        i+=1
        sum+=val
        out.append(round(sum/i))
    print("PrefixedAvg out Array is", out)

    ##2_MaxMinSortedUnSorted
    # FirstMaxMinUnSorted
    inp=[2,2,3,1]
    max1=-sys.maxsize
    min1= sys.maxsize
    oldmax=-sys.maxsize
    thirdoldmax=-sys.maxsize
    oldmin=sys.maxsize
    for i in inp:
        if i > max1:
            thirdoldmax = oldmax
            oldmax = max1
            max1 = i
        elif i > oldmax and i < max1:
            oldmax = i
        elif i > thirdoldmax and i < max1 and i < oldmax:
            thirdoldmax = i
        if i < min1:
            oldmin = min1
            min1 = i
        elif i < oldmin:
            oldmin = i
    print("First Max element == ",max1)
    print("Second Max element == ",oldmax)
    # print("First Min element == ",min1)
    # print("Second Min element == ",oldmin)
    print("Third max element == ",thirdoldmax)


    ##3 Kth largest element
    inp=[9,2,4,5,6,7]
    inp.sort()
    k = 3
    s = len(inp)
    for i in range(1,k+1):
        print(str(i) + "th largest element is ",inp[s-i])

    ## traverse only half
    inp=[9,2,41,19,117,6,5,45,12,34,555,1,3,90]
    maxvalue=0
    end = len(inp)-1
    mid = round(len(inp)/2)
    loops=0
    for x in range(0,mid+1):
        if x<end:
            loops+=1
            if inp[x] > maxvalue:
                maxvalue = inp[x]
            if inp[end] > maxvalue:
                maxvalue = inp[end]
            end-=1
    print(maxvalue)
    print("Times Loop executed ", loops, " for inp size", len(inp))

    ## traverse only 1/3
    inp=[-5,-8,-9,-50,-1,-4]
    end = len(inp)-1
    mid = round(len(inp)/3)
    loops=0
    largest=-45343
    currlist=[]
    for x in range(0,len(inp),3):
        loops+=1
        if x+1 <= len(inp)-1:
            y =x+1
        if x+2 <= len(inp)-1:
            z= x+2
        currlist=[inp[x],inp[y],inp[z],largest]
        largest= max(currlist)
    print(largest)
    print("Times Loop executed ", loops, " for inp size", len(inp))


def thirdMax(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if (len(nums)==1):
        return nums[0]
    if (len(nums)==2):
        return (max(nums[0],nums[1]))
    maxvalue=-sys.maxsize
    oldmaxvalue=-sys.maxsize
    thirdoldmax=sys.maxsize
    for i in nums:
        if i > maxvalue:
            thirdoldmax=oldmaxvalue
            oldmaxvalue=maxvalue
            maxvalue=i
        elif i > oldmaxvalue and i < maxvalue:
            thirdoldmax=oldmaxvalue
            oldmaxvalue = i
        elif i > thirdoldmax and i < maxvalue and i < oldmaxvalue:
            thirdoldmax = i
    if thirdoldmax==-sys.maxsize:
        thirdoldmax = maxvalue
    return thirdoldmax

def main():
    # callAll()
    nums=[1,2,2,5,3,5]
    print(thirdMax(nums))

if __name__ == '__main__':
    main()