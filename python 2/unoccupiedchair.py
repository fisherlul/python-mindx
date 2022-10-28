import heapq
class Solution:
    def smallestChair(times: list, targetFriend: int):
        queue_den = []
        queue_di = []

        for i in range(len(times)):
            queue_den.append((times[i][0], i))
            queue_di.append((times[i][1], i))

        queue_den.sort()
        queue_di.sort()

        dictionary = {} 
        occupied = [0] * len(times)

        for index in range(len(times)*2):
            if queue_den and queue_di and queue_den[0][0] < queue_di[0][0]:
                arr, index = heapq.heappop(queue_den)
                dictionary[index] = occupied.index(0)
                occupied[dictionary[index]] = 1

                if index == targetFriend:
                    break
            elif queue_den and queue_di and queue_den[0][0] >= queue_di[0][0]:

                dep, index = heapq.heappop(queue_di)
                occupied[dictionary[index]] = 0

        return dictionary[index]
print(Solution.smallestChair([[1,4],[2,3],[4,6]], 1))
