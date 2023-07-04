"""
Write a function that accepts a number as an input and returns
a list of integers that stretch from 0 up to the given number
(including the number!) in the increments of 5. But your list must EXCLUDE
any numbers that can be divided by 7 without a remainder.

1. We only pass one integer to the function that is int > 0

THINGS TO PAY ATTENTION TO:
Here is an example: 
--------------------
Input: 50
Output: [5, 10, 15, 20, 25, 30, 40, 45, 50]

NB: the result list excludes 0 and 35, because:

 0 divide by 7 is 0 (no remainder)
 35 divide by 7 is 5 (no remainder)

"""
def increments_of_5(number):
    result = []
    for i in range(0, number + 1, 5):
        if i % 7 != 0:
            result.append(i)
    return result

result = increments_of_5(50)
print(result)




############################################################################

"""

Write a function that will take two whole numbers (integers) as 
input and output. The  function returns the result of multiplying these two 
numbers together. For example 5 * 4 = 20

However, to make this task more challenging, you have to assume the * key of 
your keyboard is broken or missing and hence you are not allowed to use the * 
operator in your code!!!

"""

def multiply(x: int, y: int) -> int:
    total = x
    for i in range(y - 1):
        total += x
    return total

result = multiply(2, 4)
print(result)

"""
ONLY IF a student is struggling, give them a HINT:

5 * 4 = 5 + 5 + 5 + 5
7 * 6 = 7 + 7 + 7 + 7 + 7 +7
8 * 3 = 8 + 8 +8
"""
