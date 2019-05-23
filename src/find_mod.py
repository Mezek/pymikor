from math import *

# Python program to find (a^b) mod m for a large 'a'
def aModM(s, mod):
    number = 0

    # convert string s[i] to integer which gives
    # the digit value and form the number
    for i in range(len(s)):
        number = (number * 10 + int(s[i]))
        number = number % m

    return number


# Returns find (a^b) % m
def ApowBmodM(a, b, mod):
    # Find a%m
    ans = aModM(a, m)
    mul = ans

    # now multiply ans by b-1 times and take
    # mod with m
    for i in range(1, b):
        ans = (ans * mul) % m

    return ans


# Driver program to run the case
a = "512512512512"
b, m = 13, 1009
print(aModM(a, m))
print(ApowBmodM(a, b, m))

