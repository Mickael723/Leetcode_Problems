from collections import deque
class Solution:
    def timeRequiredToBuy(self, tickets: list, k: int) -> int:

        time = 0

        index = 0

        while tickets[k] > 0:

            if tickets[index] == 0:
                index += 1
                if index > len(tickets) - 1:
                    index = 0
                continue

            tickets[index] -= 1
            time += 1
            index += 1
            if index > len(tickets) - 1:
                index = 0

        return time



if __name__=="__main__":
    s = Solution()
    print(s.timeRequiredToBuy(tickets = [2,3,2], k = 2))
    print(s.timeRequiredToBuy([5,1,1,1], k = 0))