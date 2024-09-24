class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()

        def get_next_num(n):
            output = 0
            while n:
                d1 = n % 10
                output += d1**2
                n = n // 10
            return output
        
        while n not in visit:
            visit.add(n)

            n = get_next_num(n)

            if n == 1:
                return True
        return False
