class Pair:
    def __init__(self,first,second):
        self.first = first
        self.second = second

def mergeintervals(v):
    res = []
    res.append(Pair(v[0].first,v[0].second))

    for i in range (1,len(v)):
        n = len(res)
        x1=  v[i].first
        y1=  v[i].second
        x2 = res[n-1].first
        y2 = res[n-1].second

        if y2 >= x1:
            res[n-1].second = max(y1,y2)
        else:
            res.append(Pair(x1,y1))

    return res

# v = [Pair(1,5),Pair(3,7),Pair(4,6),Pair(6,8)]
# v = [Pair(10,12),Pair(12,15)]
v = [Pair(5,7),Pair(8,9)]
res = mergeintervals(v)
for i in res:
    print(i.first, i.second)


