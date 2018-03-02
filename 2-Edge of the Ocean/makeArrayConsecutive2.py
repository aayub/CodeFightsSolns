'''
PROBLEM:
Ratiorg got statues of different sizes as a present from CodeMaster for his birthday, each statue having an non-negative integer size. Since he likes to make things perfect, he wants to arrange them from smallest to largest so that each statue will be bigger than the previous one exactly by 1. He may need some additional statues to be able to accomplish that. Help him figure out the minimum number of additional statues needed.

Example:
For statues = [6, 2, 3, 8], the output should be
makeArrayConsecutive2(statues) = 3.

Ratiorg needs statues of sizes 4, 5 and 7.

Guaranteed constraints:
1 ≤ statues.length ≤ 10,
0 ≤ statues[i] ≤ 20
which means that the array is no longer than 10 elements
and no number inside the array is higher than 20

'''
def makeArrayConsecutive2(statues):
    # My Solution:
    # a) First, sorting the array from least to greatest would make this process simpler,
    # thankfully there's a built in method for that ( called .sort())
    # b) fL loops from 0 to the second last element in the array (also look at the while statement)
    # c) sL loops from 1 to the last element in the array (also look at the while statement)
    # d) the differences variable keeps track of the number of statues needed to fill in between two consecutive numbers
    # so say the numbers were 5 and 9, differences would hold 3 because you need three statues (6,7,8) to go in-between those two numbers.
    # e) Inside the while loop, it records the number of statues that can go in-between every adjacent pairs.
    # f) Inside the if statement, if difference between two consecutive number is more than one (ie. The difference between 6 and 7 is 1, but you cant put a statue in-between, so we look for a difference of higher than 1 for each consecutive pairs).
    # g) fL and sL are incremented by 1 as they continue the loop.


    # a
    statues.sort()
    # b
    fL = 0
    # c
    sL = 1
    lastItem = len(statues)-1
    # d
    differences = 0
    # e
    while (fL <= lastItem - 1) and (sL <= lastItem):
        # f
        if statues[sL] - statues[fL] > 1:
            differences += (statues[sL] - statues[fL] - 1)
        # g
        fL += 1
        sL += 1

    return differences