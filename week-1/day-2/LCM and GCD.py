import math

class Solution:
    def lcmAndGcd(self, a, b):
        gcd_value = math.gcd(a, b)
        lcm_value = (a * b) // gcd_value
        return [lcm_value, gcd_value]