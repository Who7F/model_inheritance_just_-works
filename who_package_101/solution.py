import heapq

class Solution:
    def __init__(self):
        self.help_me = 'Help text'
        self.start_sol()

    def start_sol(self):
        print('Pertinent class. no not modified')

    def help(self):
        try:
            print(self.help_me)
        except:
            print('Error. self.help_me not found')

    def Solution(self, n):
        return 0

class LastStoneWaight(Solution):
    def __init__(self):
        self.help_me = 'def Solution(list[int]) => int\nWhat is does' 
    def Solution(self, n):
        heapq._heapify_max(n)
        while len(n) > 1:    
            x = heapq._heappop_max(n)
            y = heapq._heappop_max(n)
            if x != y:
                heapq.heappush(n, x-y)
                heapq._heapify_max(n)
        return n

class isWarmer(Solution):
    def __init__(self):
        self.help_me = 'def Solution(list[int]) => list[int]\nWhat is does'
    def Solution(self, n):
        answer = [0] * len(n)
        stack = []
        for i in range(len(n)):
            while stack and stack[-1][1] < n[i]:
                x = stack.pop()[0]
                answer[x] = i -x
            stack.append((i, n[i]))    
        return answer

def main():
    x = Solution()
    x.help()
    print(x.Solution([4, 4, 5, 6, 3]))

if __name__== '__main__':
    main()
