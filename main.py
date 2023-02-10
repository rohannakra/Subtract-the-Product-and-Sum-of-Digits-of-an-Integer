# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

def subtract_product_and_sum(n):
    digits = [int(str_n) for str_n in str(n)]
    sm = sum(digits)
    product = 1
    
    for digit in digits:
        product *= digit

    return product - sm

print(subtract_product_and_sum(234))
print(subtract_product_and_sum(4421))

# ------------------------------------------------------------------------------------

# Accepted LeetCode Solution:

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = [int(str_n) for str_n in str(n)]
        sm = sum(digits)
        product = 1
    
        for digit in digits:
            product *= digit

        return product - sm
