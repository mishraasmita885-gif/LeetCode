class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max = 0
        for customer in accounts:
            total = sum(customer)

            if(max<total):
                max=total

        return max
        
    
        