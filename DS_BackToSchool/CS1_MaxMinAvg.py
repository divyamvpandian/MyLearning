import sys
# CS1
##1_PrefixAverage

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
inp=[2,4,9,6,10]
max1=-sys.maxsize
min1= sys.maxsize
oldmax=-sys.maxsize
oldmin=sys.maxsize
for i in inp:
    if i > max1:
        oldmax = max1
        max1 = i
    elif i > oldmax:
        oldmax = i
    if i < min1:
        oldmin = min1
        min1 = i
    elif i < oldmin:
        oldmin = i
print("First Max element == ",max1)
print("Second Max element == ",oldmax)
print("First Min element == ",min1)
print("Second Min element == ",oldmin)

##3 Kth largest element
inp=[9,2,4,5,6,7]
inp.sort()
k = 3
s = len(inp)
for i in range(1,k+1):
    print(str(i) + "th largest element is ",inp[s-i])

## traverse only half
inp=[9,2,4,19,6,117]
max=0
end = len(inp)-1
mid = round(len(inp)/2)
for x in range(0,mid+1):
    if inp[x] > max:
        max = inp[x]
    if inp[end] > max:
        max = inp[end]
    end-=1
print(max)

## traverse only 1/3
inp=[9,2,41,19,117,6]
end = len(inp)-1
mid = round(len(inp)/3)
x=0
for loop in range(0,mid):
    y =x+1
    z= x+2
    l = [inp[x],inp[y],inp[z]]
    maxe = max(l)
    x+=3
print(maxe)

