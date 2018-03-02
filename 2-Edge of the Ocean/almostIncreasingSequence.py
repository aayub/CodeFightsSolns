'''
PROBLEM:
Given a sequence of integers as an array, determine whether it is possible to
obtain a strictly increasing sequence by removing no more
than one element from the array.
'''

def almostIncreasingSequence(sequence):
    # My solution:
    #This function first calls on the increasingSequence function to determine
    #if the sequence is strictly increasing to begin with:
        #a) If its strictly increasing return True
        #b) If its not strictly increasing, call the removeTroubleSpot function
        #to generate a new sequence that removes the fL (aka troubleSpot) number
        #that is causing the sequence to not be strictly increasing.
        #c) Feed the new sequence from the removeTroubleSpot function into
        #the increasingSequence function again, it returns True, than the sequence
        #is almost increasing.

    check_strictlyincreasing = increasingSequence(sequence)
    print(str(check_strictlyincreasing))
    # b
    if check_strictlyincreasing != type(bool):
        # b
        modified = removeTroubleSpot(sequence, check_strictlyincreasing)
        # c
        if increasingSequence(modified) == type(bool):
            result =  True
        else:
            result = False
    # a
    else:
        result = True

    return result


def increasingSequence(seq):
    '''
    Given a sequence, the function returns True if its strictly
    increasing. Otherwise, returns the troubleSpot (where troubleSpot
    is the fL value that is causing the sequence to become False).
    >>> increasingSequence([1,3,9,10])
    True
    >>> increasingSequence([1, 4, 6, 6])
    2
    >>> increasingSequence([1, 2, 5, 5, 5])
    2
    '''
    if len(seq) == 1:
        result = True

    else:

        #indices
        fL = 0
        sL = 1
        lastItem = len(seq)-1
        increasing = True
        troubleSpot = 0
        # fL loops til the second last item in the list.
        # sL loops til the last item in the list.
        # the loop stops when both fL and sL have reached their 'final' spot
        while (fL <= lastItem-1) and (sL <= lastItem):
            if seq[fL] >= seq[sL]:
                increasing = False
                troubleSpot = fL
            # increment fL and sL
            fL +=1
            sL +=1

        # return either the bool True or an integer
        if increasing == False:
            result = troubleSpot
        else:
            result = increasing
        return result


def removeTroubleSpot(seq,troubleSpot):
    '''
    When the result from the increasingSequence function is
    False, this function removes the value at the troubleSpot
    index and returns a new sequence without seq[troubleSpot].
    '''
    seq.pop(troubleSpot)
    result = seq
    return result