class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for customer in accounts:
            customer_wealth = 0
            for bank_account in customer:
                customer_wealth += bank_account
            if customer_wealth > max_wealth:
                max_wealth = customer_wealth
        return max_wealth
