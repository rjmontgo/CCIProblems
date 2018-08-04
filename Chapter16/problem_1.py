# Using an array as a way to pass both integers by reference since
# python would pass integers by value. We can return this array and the
# first index should contain the data from the second index and vice-versa
def inPlaceSwap(arr):
    arr[0] ^= arr[1]
    arr[1] ^= arr[0]
    arr[0] ^= arr[1]
    return arr
