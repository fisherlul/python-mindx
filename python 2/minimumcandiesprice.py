cost = [6,5,7,9,2,2]
class Solution:
    def minimumCost(cost: list) -> int:
        minimum = 0
        bought = 0
        cost.sort(reverse=True)
        for i in range(len(cost)):
            if bought == 2:
                bought = 0
                continue
            minimum += cost[i]
            bought += 1
        
        return minimum
    
print(Solution.minimumCost(cost))