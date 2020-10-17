def main():
    arr = [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1]
    rearrange(arr)


def rearrange(arr):
    left = 0
    right = len(arr) - 1
    for i in range(0, round(len(arr) / 2)):
        while (arr[left] == 0):
            left += 1
        while (arr[right] == 1):
            right -= 1
        if right > left:
            temp = arr[left]
            arr[left] = arr[right]
            arr[right] = temp
    print(arr)

    # Stock prices on consecutive days
    price = [7, 1, 5, 3, 6, 4]
    n = len(price)

    # Fucntion call
    print(maxProfit(price))


def maxProfit(prices):
    if len(prices) <= 1:
        return 0
    max_profit = 0
    lowest = prices[0]
    for price in prices:
        lowest = min(lowest, price)
        max_profit = max(max_profit, price - lowest)
    return max_profit


if __name__ == '__main__':
    main()
