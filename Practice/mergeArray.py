import math

# t = int(input())
# for i in range(t):
#     n1,n2 = map(int,input().split())
#     arr1 = list(map(int,input().split()))
#     arr2 = list(map(int,input().split()))
#     arr1 = arr1 + arr2
#     arr1.sort()
#     #arr2 = arr1[n1:n2+n1]
#     #arr1 = arr1[:n1]
#     for i in arr1:
#         print(i,end=" ")
#     print()
#     t = t -1

inp=[2,4,9,6,7]
# out=[]
# temp = 0
# for i in inp:
#     inp.get(i)
#     out.append(temp+i)
#     temp = temp + i
# print(out)
#     max1=0
#     olddmax1=0
#     for i in inp:
#         if i > max1:
#             olddmax1 = max1
#             max1 = i
#     print(olddmax1)

max=0
end = len(inp)-1
mid = round(len(inp)/2)
print(mid)
for x in range(0,mid+1):
    if inp[x] > max:
        max = inp[x]
    if inp[end] > max:
        max = inp[end]
    end-=1
print(max)



