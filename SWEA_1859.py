m = int(input())
for t in range(1, m+1):
    N = int(input())
    price_list = list(map(int, input().split()))

    max_price = price_list[-1]
    gain = 0

    for i in range(N-2, -1, -1):
        if price_list[i] >= max_price:
            max_price = price_list[i]
        else:
            gain += max_price - price_list[i]

    print("#{0} {1}".format(t, gain))