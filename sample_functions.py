'''This will be a collection of our first set of functions'''

# our first function
def max_of_three(arg1, arg2, arg3):
    '''This function takes in three functions and returns the largest value'''
    if (arg1>arg2 and arg1>arg3):
            return arg1
    elif (arg2>arg3):
            return arg2
    else:
            return arg3

def list_ends(L):
    '''This function takes in a list and returns a new list with the first and last values of the original list'''
    return [L[0],L.pop()]
