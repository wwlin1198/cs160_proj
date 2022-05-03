#/usr/bin/python3
from implement_hw import magic_stones_topdown, magic_stones_bottomup, count_flips
from time import process_time

def runtime_TD():

    # Test "magic stones" problem top down
    t1_start = process_time() 
    stones = [1, 4, 6, 11, 25]
    health = 228
    magic_stones_topdown(stones, health)
    t1_stop = process_time()
    print("Elapsed time:", t1_stop, t1_start)
    return t1_stop - t1_start 
   
def runtime_BU():
    # Test "magic stones" problem bottom up
    t1_start = process_time() 
    stones = [1, 4, 6, 11, 25]
    health = 228
    magic_stones_bottomup(stones, health)
    t1_stop = process_time()
    print("Elapsed time:", t1_stop, t1_start) 
    return t1_stop - t1_start

def runtime_coin():

    # Test "count flips" problem
    t1_start = process_time() 
    arr = [4, 1, 2, 1]
    count_flips(arr) == 4
    t1_stop = process_time()
    print("Elapsed time:", t1_stop, t1_start) 
    
    return t1_stop - t1_start






if __name__ == "__main__":
   
    runtime_TD()
    runtime_BU()
    runtime_coin()



