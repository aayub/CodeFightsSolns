'''
PROBLEM: This question has images associated with it, with a general pattern of:
n(1) = 1
n(2) = 5
n(3) = 13
n(4) = 25 ...etc

Example:
For n = 2, the output should be
shapeArea(n) = 5
For n = 3, the output should be
shapeArea(n) = 13.
'''
def shapeArea(n):
    # My Solution:
    # Given n, the function returns: (n)^2 + (n-1)^2
    output = (n**2)+ ((n-1)**2)
    return output