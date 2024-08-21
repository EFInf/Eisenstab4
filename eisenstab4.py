# Bottom-up: with a loop, memoization and best solution
#

prices = [0,1,1,3,5,5,7,9,8,10,10]
best_cut_price = []
best_solution = []
m = len(prices)

for n in range(m):
    best = prices[n]
    bestsol = [n]
    for i in range(1,n):
        if best_cut_price[i]+prices[n-i]>best:
            best = best_cut_price[i]+prices[n-i]
            bestsol = best_solution[i]+[n-i]
    best_cut_price.append(best)
    best_solution.append(bestsol)

for i in range(m):
    print(f"Best cut for rod of length {i}:\n Best price: {best_cut_price[i]} \n Best cut: {best_solution[i]}")