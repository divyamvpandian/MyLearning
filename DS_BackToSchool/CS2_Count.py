def main():
    n=10
    sum=0
    for i in range(1,n+1):
        sum+=i
    print(sum)
    print(round((n*(n+1))/2))

    ##Collapse the list

    list=[None for i in range(0,10)]

    list[1]="A"
    list[2]="B"
    list[4]="C"
    list[6]="D"
    list[9]="E"
    print(list)
    replacepos = len(list)-1
    currpos =len(list)-1
    for item in reversed(list):
        if item!=None:
            list[currpos] = None
            list[replacepos] = item
            replacepos-=1
        currpos-=1
    print(list)


if __name__ == '__main__':
    main()

