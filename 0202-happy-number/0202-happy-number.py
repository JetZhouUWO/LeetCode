class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()

        def get_next_number(n):
            output = 0
            while n:
                num = n % 10
                output += num**2
                n = n // 10
            return output

        while n not in visit:
            visit.add(n)
            n = get_next_number(n)
            if n == 1:
                return True
        return False