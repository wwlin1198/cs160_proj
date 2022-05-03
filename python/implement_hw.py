#########################################################
##  Implementation of HW 5 Question 1, CS160 Spring22  ##
#########################################################

# Input: array (of ints) of stone damage values, and dragon health value (int)
# Returns: integer, the minimum number of stones needed to kill the dragon
# Implemented using top-down dynamic programming

#/usr/bin/python3
from cmath import inf
from itertools import count


def magic_stones_topdown(stones, health):

    stone_cache = {}
    return calc_stones(stones,health,stone_cache)

def calc_stones(stones,health,stone_cache):

    if health in stone_cache:
        return stone_cache[health]

    if health == 0:
        stone_cache[health] = 0
    elif health < 0:
        stone_cache[health] = inf
    else:
        chosen = []
        for i in stones:
            chosen.append(calc_stones(stones,health - i,stone_cache))
        stone_cache[health] = min(chosen)+1
            
    return calc_stones(stones,health,stone_cache)
# Input: array (of ints) of st one damage values, and dragon health value (int)
# Returns: integer, the minimum number of stones needed to kill the dragon
# Implemented using bottom-up dynamic programming
def magic_stones_bottomup(stones, health):

    table = [[0 for i in range(health + 1)] for i in range(len(stones) + 1)]

    # Loop to initialize the array
    # as infinite in the row 0
    for i in range(1, health + 1): table[0][i] = inf
 
    for i in range(1, len(stones) + 1):
 
        for j in range(1, health + 1):
            if (stones[i - 1] > j):
                table[i][j] = table[i - 1][j]
            else:
                table[i][j] = min(table[i - 1][j],table[i][j - stones[i - 1]] + 1)
 
    return table[len(stones)][health]

#########################################################
##  Implementation of HW 2 Question 2, CS160 Spring22  ##
#########################################################

# Input: array of integers
# Returns: integer, the number of flips in the array
def _mergeSort(arr, temp_arr, left, right):
 
    # A variable inv_count is used to store
    # inversion counts in each recursive call
 
    inv_count = 0
 
    # We will make a recursive call if and only if
    # we have more than one elements
 
    if left < right:
 
        # mid is calculated to divide the array into two subarrays
        # Floor division is must in case of python
 
        mid = (left + right)//2
 
        # It will calculate inversion
        # counts in the left subarray
 
        inv_count += _mergeSort(arr, temp_arr,
                                left, mid)
 
        # It will calculate inversion
        # counts in right subarray
 
        inv_count += _mergeSort(arr, temp_arr,
                                mid + 1, right)
 
        # It will merge two subarrays in
        # a sorted subarray
 
        inv_count += merge(arr, temp_arr, left, mid, right)
    return inv_count
 
# This function will merge two subarrays
# in a single sorted subarray
 
 
def merge(arr, temp_arr, left, mid, right):
    i = left     # Starting index of left subarray
    j = mid + 1  # Starting index of right subarray
    k = left     # Starting index of to be sorted subarray
    inv_count = 0
 
    # Conditions are checked to make sure that
    # i and j don't exceed their
    # subarray limits.
 
    while i <= mid and j <= right:
 
        # There will be no inversion if arr[i] <= arr[j]
 
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            k += 1
            i += 1
        else:
            # Inversion will occur.
            temp_arr[k] = arr[j]
            inv_count += (mid-i + 1)
            k += 1
            j += 1
 
    # Copy the remaining elements of left
    # subarray into temporary array
    while i <= mid:
        temp_arr[k] = arr[i]
        k += 1
        i += 1
 
    # Copy the remaining elements of right
    # subarray into temporary array
    while j <= right:
        temp_arr[k] = arr[j]
        k += 1
        j += 1
 
    # Copy the sorted subarray into Original array
    for loop_var in range(left, right + 1):
        arr[loop_var] = temp_arr[loop_var]
 
    return inv_count

def count_flips(arr):
    temp_arr = [0]*len(arr)
    return _mergeSort(arr, temp_arr, 0, len(arr)-1)

