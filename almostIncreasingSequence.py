""" 
Example

For sequence = [1, 3, 2, 1], the output should be
almostIncreasingSequence(sequence) = false;

There is no one element in this array that can be removed in order to get a strictly increasing sequence.

For sequence = [1, 3, 2], the output should be
almostIncreasingSequence(sequence) = true.

You can remove 3 from the array to get the strictly increasing sequence [1, 2]. Alternately, you can remove 2 to get the strictly increasing sequence [1, 3].
"""

def almostIncreasingSequence(sequence):
    noIncreasing = 0
    length = len(sequence)
    for i in range(length-1):
        for j in range(i+1, length):
            if sequence[i] > sequence[j]:
                noIncreasing += 1

    if noIncreasing > 1:
    	return False
    else:
    	return True

    
