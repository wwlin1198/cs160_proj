#/usr/bin/python3
from implement_hw import magic_stones_topdown, magic_stones_bottomup, count_flips
from time import process_time
from matplotlib import pyplot as plt
from implement_hw import magic_stones_topdown, magic_stones_bottomup, count_flips
import numpy as np


def runtime_TD(TDSC,TDSChealth):

    # Test "magic stones" problem top down
    t1_start = process_time() 
    stones = [1, 4, 6, 11, 25]
    health = 6
    for i in range(50):
        magic_stones_topdown(stones, health)
        t1_stop = process_time()
        print("Elapsed time:", t1_stop, t1_start)
        time =  t1_stop - t1_start
        TDSC.append(time)
        TDSChealth.append(health)
        health+= 2

def runtime_TD2(TDSC2,TDSChealth2):
    
    # Test "magic stones" problem top down
    t1_start = process_time() 
    stonesnum = 1
    health = 100
    for i in range(10):
        stones = np.random.rand(stonesnum)
        magic_stones_topdown(stones, health)
        t1_stop = process_time()
        print("Elapsed time:", t1_stop, t1_start)
        time =  t1_stop - t1_start
        TDSC2.append(time)
        TDSChealth2.append(health)
        stonesnum+= 2
   
def runtime_BU(TDSBU,TDBUhealth):
    # Test "magic stones" problem bottom up
    t1_start = process_time() 
    stones = [1, 4, 6, 11, 25]
    health = 6
    for i in range(50):
        magic_stones_bottomup(stones, health)
        t1_stop = process_time()
        time =  t1_stop - t1_start
        TDSBU.append(time)
        TDBUhealth.append(health)
        health+= 2

def runtime_BU2(TDSBU2,TDBUhealth2):
    # Test "magic stones" problem bottom up
    t1_start = process_time() 
    stonesnum = 1
    health = 100
    for i in range(10):
        stones = np.random.rand(stonesnum)
        magic_stones_bottomup(stones, health)
        t1_stop = process_time()
        time =  t1_stop - t1_start
        TDSBU2.append(time)
        TDBUhealth2.append(health)
        stonesnum+= 2

def runtime_coin(flips,flip_size):

    # Test "count flips" problem
    increment = 1
    arr = list(np.random.randint(200, size= increment))
    for i in range(10):
        t1_start = process_time() 
        count_flips(arr)
        t1_stop = process_time()
        print("Elapsed time:", t1_stop, t1_start) 
        time =  t1_stop - t1_start
        flips.append(time)
        flip_size.append(increment)
        increment = increment * 2








if __name__ == "__main__":

    TDSC = []
    TDSChealth = []


    TDSC2 = []
    TDSChealth2 = []

    TDSBU = []
    TDBUhealth = []

    TDSBU2 = []
    TDBUhealth2 = []

    TDCF = []
    TDCFF = []

    flips = []
    flip_size = []
   
    runtime_TD(TDSC,TDSChealth)
    runtime_TD2(TDSC2,TDSChealth2)
    runtime_BU(TDSBU,TDBUhealth)
    runtime_BU2(TDSBU2,TDBUhealth2)
    runtime_coin(flips,flip_size)

 

    y = np.array(TDSC)
    x = np.array(TDSChealth)
    poly = np.polyfit(x, y, deg=5)
    fig, ax = plt.subplots()
    ax.set_title('Magical Stones Top Down Constant Stones, Health Increments by 2')
    ax.plot(y,'o', label='Size')
    ax.plot(np.polyval(poly, x), label='Time')
    ax.legend()
    plt.show()

    y = np.array(TDSC2)
    x = np.array(TDSChealth2)
    poly = np.polyfit(x, y, deg=5)
    fig, ax = plt.subplots()
    ax.set_title('Magical Stones Top Down Constant Health, Number Stones Increment by 2')
    ax.plot(y,'o', label='Size')
    ax.plot(np.polyval(poly, x), label='Time')
    ax.legend()
    plt.show()

    y = np.array(TDSBU)
    x = np.array(TDBUhealth)
    poly = np.polyfit(x, y, deg=5)
    fig, ax = plt.subplots()
    ax.set_title('Magical Stones Bottom Up Constant Stones, Health Increments by 2')
    ax.plot(y,'o', label='Size')
    ax.plot(np.polyval(poly, x), label='Time')
    ax.legend()
    plt.show()

    y = np.array(TDSBU2)
    x = np.array(TDBUhealth2)
    poly = np.polyfit(x, y, deg=5)
    fig, ax = plt.subplots()
    ax.set_title('Magical Stones Bottom Up Constant Health, Number Stones Increment by 2')
    ax.plot(y,'o', label='Size')
    ax.plot(np.polyval(poly, x), label='Time')
    ax.legend()
    plt.show()

    y = np.array(flip_size)
    x = np.array(flips)
    print(flips,flip_size)
    poly = np.polyfit(x, y, deg=10)
    fig, ax = plt.subplots()
    ax.set_title('Coin flip doubling')
    ax.plot(y,'o', label='Size')
    ax.plot(np.polyval(poly, x), label='Fit')
    ax.legend()
    plt.show()








