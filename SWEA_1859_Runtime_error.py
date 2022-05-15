m = int(input())
for t in range(1, m+1):
    N = int(input())
    price_list = list(map(int, input().split()))
    gain = 0
    pre_gain = 1

    while pre_gain != gain and N != 0:
        pre_gain = gain
        price_list_reverse = price_list.copy()
        price_list_reverse.reverse()
        max_price = max(price_list)
        max_index = price_list_reverse.index(max_price)
        max_index = N - 1 - max_index
        gain += max_price*max_index - sum(price_list[ : max_index])
        del price_list[: max_index + 1]
        N = len(price_list)
    print("#{0} {1}",format(t, gain))