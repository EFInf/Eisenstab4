# Top-down: with recursion and memoization
#

prices = [0,1,1,3,5,5,7,9,8,10,10]
best_cut_price = [0]
def best_cut(n):
    if len(best_cut_price)<=n:
        best = prices[n]
        for i in range(n):
            if best_cut_price[i]+prices[n-i]>best:
                best = best_cut_price[i]+prices[n-i]
        best_cut_price.append(best)
    return best_cut_price[n]

for i in range(len(prices)):
    print(f"Best cut for rod of length {i}: {best_cut(i)}")