class Solution:
    def isHappy(self, n: int) -> bool:
        # set up a set to prevent infinite loop
        visit = set()

        def get_next_number(n):
            output = 0
            while n != 0:
                digit = n % 10
                output += digit **2
                n = n // 10
            
            return output

        while n not in visit:
            visit.add(n)
            n = get_next_number(n)
            if n == 1:
                return True

        return False
        