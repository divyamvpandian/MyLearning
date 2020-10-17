from stack import Stack

def main():
    # n = 5
    # fibonaccirec(n)
    # fibonacci(n)
    # print(computeefficientGCD(357,234))
    # nums = [1,2,3,3,3,4,5,5,6]
    # dedups(nums)
    # countloops()
    # print(nums)
    # countDups(nums)
    # arr=[6,3,8,10,16,7,5,2,9,14,1]
    # pairwuithsum(arr,10)
    # arr=[1,3,4,5,6,8,9,10,12,14]
    # pairwuithsuminsorted(arr,10)
    # str = "abcde"
    # print(finddupsinstr(str))
    # str="ABC"
    # print(putil(str))
    # arr1=[1,12,15,26,38]
    # arr2=[2,13,17,30,45]
    # median(arr1,arr2)
    # vals = [60,100,120]
    # wt = [10,20,30]
    # maxWeight = 50
    # n = len(wt)
    # t = [[-1 for i in range(maxWeight+ 1)] for j in range(n + 1)]
    # print(len(t[0]))
    # print(knapsack(wt,vals,maxWeight,n))
    # arr=[1,10,20,0,4,5,0,7,0]
    # arr = movezerostoleft(arr)
    # print(arr)
    # input = "geeks quiz practice code"
    # reverstr(input)
    # input = " "
    # result = str_to_int(input)
    # dec_num = 242
    # convert_int_to_bin(dec_num)
    # print(search("pad"));
    # print(search("bad"));
    # print(search(".ad"));
    # print(search("b.."));
    # generateprime(10,30)
    # arr=[1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 6, 6]
    # # print(searchinrotated(arr,4,0,len(arr)-1))
    # # print(ispalindrome("abcra"))
    # # arr=[24,56,78,64,32,12,9,100,98]
    # # sortdes(arr)
    # print(lowhigh(arr,2))
    # A = [1,2,3,4]
    # queries = [[1,0],[-3,1],[-4,0],[2,3]]
    # result = sumEvenAfterQueries(A,queries)
    # str=""
    # print(longestsubseq(str))
    print(checkrotation([1,2,3,4,5,6],[2,3,7,5,6,1]))

def checkrotation(arr1,arr2):
    n = len(arr1)
    m=len(arr2)
    if n!=m:
        return False
    element = arr1[0]
    for i in range(m):
        if element == arr2[i]:
            start = i
            break
    k = 0
    j = start
    while k < n:
        if arr2[j]!=arr1[k]:
            return False
        j=(j+1)%m
        k+=1
    return True


def lowhigh(arr,x):
    i=0
    j=len(arr)-1
    low=-1
    high=-1
    count=0
    while i < j:
        count+=1
        if arr[i]==x:
            low = i
            high=-1
            break
        elif arr[j]==x:
            high = j
            low=-1
            break
        else:
            i+=1
            j-=1
    if low > 0:
        inc = low
        while arr[inc]==x:
            count+=1
            inc+=1
        high = inc-1
    if high >0:
        inc =high
        while arr[inc]==x:
            count+=1
            inc-=1
        low=inc+1
    print(count)
    return low,high
def sortdes(arr):
    newarr=[]
    cnt=0
    while arr:
        min = arr[0]
        for x in arr:
            if x > min:
                min = x
        newarr.append(min)
        arr.remove(min)
    print(cnt,newarr)



def quicksort(arr,l,h):
    if l<h:
        newp = partition(arr,l,h)
        quicksort(arr,l,newp)
        quicksort(arr,newp+1,h)
    print(arr)

def ispalindrome(str):
    i=0
    j=len(str)-1
    while i<j:
        if str[i]==str[j]:
            i+=1
            j-=1
        else:
            return False

    return True

def partition(arr,l,h):
    pivot = arr[l]
    i=l
    j=h
    while i<j:
        while arr[i]<=pivot:
            i+=1
        while arr[j]>pivot:
            j-=1
        ## swap
        if i<j:
            arr[i], arr[j]= arr[j], arr[i]
    arr[l], arr[j]= arr[j], arr[l]
    return j

def convert_int_to_bin(dec_num):
    stack = Stack()
    while dec_num > 0:
        stack.push(dec_num % 2)
        dec_num = dec_num // 2
    res = ""
    while not stack.is_empty():
        res+=str(stack.pop())
    print(res)

def search(word):
    worddictionary=["bad","dad","mad"]
    if word in worddictionary:
        return True

    if "." not in word and word not in worddictionary:
        return False
    else:
        dotcount = 0
        for c in word:
            if c==".":
                dotcount+=1
        for dictitem in worddictionary:
            matchcount=0
            if len(dictitem)==len(word):
                for i in range(0,len(word)):
                    if word[i]==".":
                        continue
                    elif word[i]==dictitem[i]:
                        matchcount+=1
                if matchcount == len(word) - dotcount:
                    return True

        return False

def str_to_int(input_str):
    n = len(input_str)
    multiple = n-1
    start = 0
    if " " in input_str:
        return -1
    if "-" in input_str[0]:
        start = 1
        multiple-=1
    result = 0
    for i in range(start,n):
        value = int(input_str[i])
        result += value*pow(10,multiple)
        multiple-=1
    if start ==1:
        result *= -1
    print(result)
    return result

def reverstr(input):
    inarr = input.split(' ')
    outstr = " ".join([str(inarr[i]) for i in range(len(inarr)-1,-1,-1)])
    print(outstr)

def movezerostoleft(arr):
    ## eg 1 10 20 0 4 5 0 7
    min=0
    i = 0
    while i < len(arr):
        if arr[i]==0:
            arr[i] = arr[min]
            arr[min]=0
            min+=1
        i+=1
    return arr

def knapsack(wt,vals,maxweight,n):

    ## Exit condition
    if n==0 or maxweight==0:
        return 0

    lastitem = wt[n-1]
    ## if the last item exceeds the weight ignore that item
    if lastitem  > maxweight:
        return knapsack(wt,vals,maxweight,n-1)
    else:
        ## if not, it will be either in the max set or not
        return max(vals[n-1] + knapsack(wt,vals,maxweight-lastitem,n-1), knapsack(wt,vals,maxweight,n-1))


def median(arr1,arr2):
    i=0
    j=0
    res = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            res.append(arr1[i])
            i+=1
        elif arr1[i] > arr2[j]:
            res.append(arr2[j])
            j+=1
    if i < len(arr1):
        while i < len(arr1):
            res.append(arr1[i])
            i+=1
    if j < len(arr2):
        while j < len(arr2):
            res.append(arr2[j])
            j+=1
    print(res)
    totalcount = len(arr1) + len(arr2)
    if totalcount%2==0:
        median = (res[totalcount//2] + res[(totalcount//2)-1]) // 2
    else:
        median = res [totalcount/2]
    print(median)

def putil(str):
    flags=[0]*len(str)
    level=0
    chararr = [" "]*len(str)
    perm(str,level,flags,chararr)

def perm(str,level,flags,chararr):
    print(flags)
    if level==len(str):
        print(chararr)
    for i in range(0,len(str)):
        if flags[i]==0:
            chararr[level] = str[i]
            flags[i]=1
            # level+=1
            perm(str,level+1,flags,chararr)
            flags[i]=0


def finddupsinstr(s):
    checker = 0
    for c in s:
        dis = ord(c) - ord('a')
        res = 1 << dis
        if checker & res > 0:
            return False
        else:
            checker = checker | res
    return True
def sumEvenAfterQueries(A, queries):
    """
    :type A: List[int]
    :type queries: List[List[int]]
    :rtype: List[int]
    """
    answer=[]
    total = sum(x for x in A if x%2==0)
    for i in range(len(queries)):
        item = queries[i]
        idx = item[1]
        value = item[0]
        total -= A[idx] %2 ==0 and A[idx]
        A[idx] = A[idx] + value
        total += A[idx] %2 ==0 and A[idx]
        queries[i]=total
    return queries

def longestsubseq(str):
    n = len(str)
    i =0
    dict={}
    res=[]
    res[:0]=str
    maxlen = 0
    start = 0
    for idx,ch in enumerate(res):
        if ch in dict:
            maxlen = max(maxlen,idx-start)
            start = idx
        else:
            dict[ch]=idx

    return maxlen


def pairwuithsuminsorted (arr,k):
    i =0
    j = len(arr)-1
    while i<j:
        if arr[i]+arr[j]==k:
            print("Pair",arr[i],arr[j])
            i+=1
            j-=1
        elif arr[i]+arr[j] > k:
            j-=1
        else:
            i+=1

def pairwuithsum(arr,k):
    dict = {}
    for i in range(0,len(arr)):
        diff = k-arr[i]
        if diff in dict:
            print("Pair is",arr[i],diff)
        dict[arr[i]] = k-arr[i]

def countDups(arr):
    prev = arr[0]
    lastDup = 0
    i = 1
    cnt = 0
    while i < len(arr):
        if arr[i]!=prev:
            prev = arr[i]
        else:
            if arr[i]!=lastDup:
                lastDup = arr[i]
                print(lastDup)
                cnt = 0
            else:
                cnt+=1
        i+=1
    print(cnt)
def multiplemissing(arr):
    low = arr[0]
    diff = low - 0
    for i in range(0,len(arr)):
        if arr[i]-i != diff:
            print("Missing element", i+diff)
            diff = arr[i]-i

def reverseArr(arr):
    end = len(arr)-1
    for i in range(end//2+1):
        temp=arr[i]
        arr[i] = arr[end]
        arr[end] = temp
        end-=1;
    print(arr)

def ifarrsorted(arr):
    prev = arr[0]
    for i in range(1,len(arr)-1):
        if arr[i] < prev:
            return False
        else:
            prev = arr[i]
    return True
def leftRotate(arr):
    start = 1
    end = len(arr)-1
    firstelement = arr[0]
    while start <= end:
        arr[start-1] = arr[start]
        start+=1
    arr[end]= firstelement
    print(arr)

def fibonacciiterlst(n):
    fiblist=[0 for i in range(0,n)]
    fiblist[0]=0
    fiblist[1]=1
    for i in range(2,n):
        fiblist[i] = fiblist[i - 1] + fiblist[i - 2]
    print(fiblist[n-1])

def fibonaccirec(n):
    if n <=1:
        return n
    else:
        return fibonaccirec(n-1)  + fibonaccirec(n-2)

def fibonacci(n):
    prev = 0
    curr = 1
    sum = 0
    i = 1
    while i < n:
        sum = prev + curr
        prev = curr
        curr = sum
        i += 1
    print(sum)


def computeGCD(a,b):
    i = 1
    mac = 0
    while i < a+b:
        if a%i==0 and b%i==0:
           mac = max(mac,i)
        i+=1
    return mac

def computeefficientGCD(a,b):
    # Euclidean Algo
    if b==0:
        return a
    else:
        c = a%b
        return computeefficientGCD(b,c)

def dedups(nums):
    i = 0
    for j in range(0, len(nums)):
        if nums[i]!=nums[j]:
            nums[i+1]=nums[j]
            i+=1
    print(nums[:i+1])

def countloops():
    i=200
    n=110
    c=0
    while i >= n:
        c+=1
        i-=1
        n+=1
    print(c)

def generateprime(a,b):
    while a<b:
        if isprime(a):
            print(a)
        a+=1

def isprime(x):
    i=2
    while i<x:
        if x%i==0:
            return False
        i+=1
    return True

def searchinrotated(arr,x,low,high):
    if low > high:
        return -1
    mid = low + (high-low) // 2
    if arr[mid]==x:
        return mid
    if arr[low] <= arr[mid]: ## left is sorted
        if x >= arr[low] and x <= arr[mid]:
            return searchinrotated(arr,x,low,mid-1)
        else:
            return searchinrotated(arr,x,mid+1,high)
    elif arr[mid]<=arr[high]:
        if x >= arr[mid] and x<=arr[high]:
            return searchinrotated(arr,x,mid+1,high)
        else:
            return searchinrotated(arr,x,low,mid-1)

if __name__ == '__main__':
    main()
