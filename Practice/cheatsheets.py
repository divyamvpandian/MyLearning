import itertools
from functools import reduce
from collections import Counter

def main():
    inl1 = [45,-6,2,3,4]
    inl2 =  range(100)
    inl3 = range(1,50)
    inl4 = inl2[1:2]

    inl1.append(5)
    inl1.extend(inl2)
    ## sorted
    print(sorted(inl1))
    print(inl2)
    print(inl3)
    ## sum
    print(sum(inl4))

    a = [1,2,3,4]
    b = [5,6,7,8]

    ## zip usage
    c = [sum(pair) for pair in zip(a,b)]

    # sort by lastname - lambda
    names =["Nat El","Divya V","Veer K","Mani U"]
    bylastname = sorted(names, key= lambda e: e.split(" ")[1])
    print(bylastname)

    l = [[1,2],[3,4]]
    fl = list(itertools.chain.from_iterable(l))
    print(fl)

    ##reduce
    res = reduce(lambda o,e : e*o, fl )
    print(res)
    print(list("Divya"))

    occurences = [1,3,4,5,5,5,6,6,7]
    print(occurences.count(5))
    print(occurences.index(7))
    occurences.insert(1,2)
    print(occurences)

    d = {1: "efwg",2:"fwgve"}
    d1 = {1: "test",2:"test2"}
    print(type(d),d.items(),d.keys(),d.values())
    d.update(d1)
    print(type(d),d.items(),d.keys(),d.values())
    val = "test2"
    mk = {k for k,v in d.items() if v==val}
    print(mk)

    colors = ["blue","blue","blue","green","yelo","or","or","or","or"]
    counter = Counter(colors)
    counter["red"]+=1
    print(counter)
    print(counter.most_common()[0])

if __name__ == '__main__':     # Runs main() if file wasn't imported.
    main()