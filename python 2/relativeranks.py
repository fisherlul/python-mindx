import heapq
class Solution:
    def findRelativeRanks(score: list[int]) -> list[str]:
        org_list = score.copy()

        heapq.heapify(score)

        selectCount = len(score)

        largests = heapq.nlargest(selectCount, score)

        for i in range(len(score)):
            if largests.index(org_list[i]) == 0:
                org_list[i] = "Gold Medal"
            elif largests.index(org_list[i]) == 1:
                org_list[i] = "Silver Medal"
            elif largests.index(org_list[i]) == 2:
                org_list[i] = "Bronze Medal"
            elif largests.index(org_list[i]) > 2:
                org_list[i] = str(largests.index(org_list[i]) + 1)
        print(org_list)
    
num = int(input("Enter number of characters: "))
new_list = []
for i in range(num):
    val = float(input(f'Enter character number {i+1}: '))
    new_list.append(val)
Solution.findRelativeRanks(new_list)