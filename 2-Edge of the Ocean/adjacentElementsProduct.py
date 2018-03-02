'''
PROBLEM:
Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.

Example:
For inputArray = [3, 6, -2, -5, 7, 3], the output should be
adjacentElementsProduct(inputArray) = 21.

7 and 3 produce the largest product, so therefore the function returns 21.
'''
def adjacentElementsProduct(inputArray):
    # My Solution:
    # a)fL loops from 0 to the second last element in the array (also look at the while statement)
    # b)sL loops from 1 to the last element in the array (also look at the while statement)
    # c)highestProduct holds the product of the first two elements as its initial value
    # d)Inside the while loop, the product variable takes the product of each adjacent pair
    # e)Inside the if statement (which is inside the loop) compares each adjacent pair value with the highestProduct
    # and if the product is higher than the highestProduct thus far, than product now becomes the highestProduct
    # f)fL and sL are incremented by 1 as they continue the loop


    # a
    fL = 0
    # b
    sL = 1
    lastItem = len(inputArray) - 1
    # c
    highestProduct = inputArray[fL]*inputArray[sL]

    while (fL <= lastItem - 1) and (sL <= lastItem):
        # d
        product = inputArray[fL]*inputArray[sL]
        if product > highestProduct:
            # e
            highestProduct = product
        # f
        fL += 1
        sL += 1

    return highestProduct
