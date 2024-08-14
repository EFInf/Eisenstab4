# Top-down: with recursion, without memoization
#

prices = [0,1,1,3,5,5,7,9,8,10,10]
def best_cut(n):
    if n<=1:
        return prices[n]
    else:
        best = prices[n]
        for i in range(n):
            besti = best_cut(i)
            if besti+prices[n-i]>best:
                best = besti+prices[n-i]
    return best

for i in range(11):
    print(f"Best cut for rod of length {i}: {best_cut(i)}")