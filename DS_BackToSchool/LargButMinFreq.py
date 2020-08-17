import os,operator

def main():
    arr = [1,2,3,4,4,4,70,70,70,50,50]
    print(getfrequency(arr))


def getfrequency(arr):
    arr.sort(reverse=True)
    freq={}
    for x in arr:
        try:
            freq[x]+=1
        except KeyError:
            freq[x]=1
    print(freq.items())
    sorted_x = sorted(freq.items(), key=operator.itemgetter(1))
    print(sorted_x)
    return sorted_x[0][0]

if __name__=='__main__':
    main()

