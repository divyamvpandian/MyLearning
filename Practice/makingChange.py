import sys

def minCoinsNeeded(coins,value,cache):
    mincoins=0
    if cache.get(value) is not None and cache.get(value) >=0:
        return cache[value]
    for coin in coins:
        if value-coin >= 0:
            value = value - coin
            if value in cache:
                return cache[value]
            else:
                mincoins = min(mincoins,minCoinsNeeded(coins,value,cache))
                cache[value]=mincoins
    return cache.get(value)


def main():
    coins=[1,5,10,25]
    coins.sort(reverse=True)
    print(coins)
    value=32
    c
    print(minCoinsNeeded(coins,value,cache))
    # print(minCoins(coins,4,value))

if __name__=="__main__":
    main()