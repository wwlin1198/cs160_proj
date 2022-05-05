import time
import numpy as np
from matplotlib import pyplot as plt
from implement_hw import magic_stones_topdown, magic_stones_bottomup, count_flips
#top down testing
testTD1 = True
testTD2 = True
testTD3 = True
testTD4 = True
testTD5 = True

#bottom up testing
testBU1 = True #Bottom up
testBU2 = True
testBU3 = True
testBU4 = True
testBU5 = True

#flips testing
testF1 = True #flips
testF2 = True
testF3 = True
testF4 = True
testF5 = True

if testTD1:
    TDSC = []
    TDSChealth = []
    print ("Timing for Top Down Magical Stones: Stones Constant")
    # Test top down "magic stones" problem
    stones = [1,10,25,100]

    health = 6
    tic = time.perf_counter()
    magic_stones_bottomup(stones, health)
    toc = time.perf_counter()
    time1 = toc - tic
    TDSC.append(time1)
    TDSChealth.append(health)

    print(toc-tic)

    health = 12
    tic = time.perf_counter()
    magic_stones_topdown(stones, health)
    toc = time.perf_counter()
    time1 = toc - tic
    TDSC.append(time1)
    TDSChealth.append(health)
    print(toc-tic)

    health = 25
    tic = time.perf_counter()
    magic_stones_topdown(stones, health)
    TDSChealth.append(health)
    toc = time.perf_counter()
    time1 = toc - tic
    TDSC.append(time1)
    print(toc-tic)

    health = 50
    tic = time.perf_counter()
    magic_stones_topdown(stones, health)
    toc = time.perf_counter()
    TDSChealth.append(health)
    time1 = toc - tic
    TDSC.append(time1)
    print(toc-tic)

    health = 100
    tic = time.perf_counter()
    magic_stones_topdown(stones, health)
    toc = time.perf_counter()
    time1 = toc - tic
    TDSC.append(time1)
    TDSChealth.append(health)
    print(toc-tic)

    health = 200
    tic = time.perf_counter()
    magic_stones_topdown(stones, health)
    toc = time.perf_counter()
    TDSChealth.append(health)
    time1 = toc - tic
    TDSC.append(time1)
    print(toc-tic)

    health = 400
    tic = time.perf_counter()
    magic_stones_topdown(stones, health)
    toc = time.perf_counter()
    time1 = toc - tic
    TDSChealth.append(health)
    TDSC.append(time1)
    print(toc-tic)

    health = 800
    tic = time.perf_counter()
    magic_stones_topdown(stones, health)
    toc = time.perf_counter()
    time1 = toc - tic
    TDSChealth.append(health)
    TDSC.append(time1)
    print(toc-tic)

    # health = 900
    # TDSChealth.append(health)
    # tic = time.perf_counter()
    # magic_stones_topdown(stones, health)
    # toc = time.perf_counter()
    # time1 = toc - tic
    # TDSC.append(time1)
    # print(toc-tic)
print(TDSChealth)
print(TDSC)

if testBU1:
    # test bottom up
    BUSC = []
    print("Timing for Bottom Up Magical Stones: Stones Constant")
    stones = [1]

    health = 6
    tic = time.perf_counter()
    magic_stones_bottomup(stones, health)
    toc = time.perf_counter()
    time1 = toc - tic
    BUSC.append(time1)
    print(toc-tic)

    health = 12
    tic = time.perf_counter()
    magic_stones_bottomup(stones, health)
    toc = time.perf_counter()
    time1 = toc - tic
    BUSC.append(time1)
    print(toc-tic)

    health = 25
    tic = time.perf_counter()
    magic_stones_bottomup(stones, health)
    toc = time.perf_counter()
    time1 = toc - tic
    BUSC.append(time1)
    print(toc-tic)

    health = 50
    tic = time.perf_counter()
    magic_stones_bottomup(stones, health)
    toc = time.perf_counter()
    time1 = toc - tic
    BUSC.append(time1)
    print(toc-tic)

    health = 100
    tic = time.perf_counter()
    magic_stones_bottomup(stones, health)
    toc = time.perf_counter()
    time1 = toc - tic
    BUSC.append(time1)
    print(toc-tic)

    health = 200
    tic = time.perf_counter()
    magic_stones_bottomup(stones, health)
    toc = time.perf_counter()
    time1 = toc - tic
    BUSC.append(time1)
    print(toc-tic)

    health = 400
    tic = time.perf_counter()
    magic_stones_bottomup(stones, health)
    toc = time.perf_counter()
    time1 = toc - tic
    BUSC.append(time1)
    print(toc-tic)

    health = 800
    tic = time.perf_counter()
    magic_stones_bottomup(stones, health)
    toc = time.perf_counter()
    time1 = toc - tic
    BUSC.append(time1)
    print(toc-tic)

if testF1:
    flips = []
    print("Testing Flips Doubling array")
    # Test "count flips" problem
    arr = [4]
    tic = time.perf_counter()
    count_flips(arr)
    toc = time.perf_counter()
    time1 = toc - tic
    flips.append(time1)
    print(toc-tic)

# Test "count flips" problem
    arr = [4, 1]
    tic = time.perf_counter()
    count_flips(arr)
    toc = time.perf_counter()
    time1 = toc - tic
    flips.append(time1)
    print(toc-tic)

# Test "count flips" problem
    arr = [4, 1, 2, 1]
    tic = time.perf_counter()
    count_flips(arr)
    toc = time.perf_counter()
    time1 = toc - tic
    flips.append(time1)
    print(toc-tic)
# Test "count flips" problem
    arr = [10,3,8,6, 4, 1, 2, 1]
    tic = time.perf_counter()
    count_flips(arr)
    toc = time.perf_counter()
    time1 = toc - tic
    flips.append(time1)
    print(toc-tic)
# Test "count flips" problem
    arr = [80,34,5,25,60,1,26,34,6,23,8,35,10,3,8,6]
    tic = time.perf_counter()
    count_flips(arr)
    toc = time.perf_counter()
    time1 = toc - tic
    flips.append(time1)
    print(toc-tic)
# Test "count flips" problem
    arr = [124,23,14,90,50,30,20,56,70,23,80,34,5,25,
           60,1,26,34,6,23,80,34,5,25,60,1,26,34,6,23,8,35]
    tic = time.perf_counter()
    count_flips(arr)
    toc = time.perf_counter()
    time1 = toc - tic
    flips.append(time1)
    print(toc-tic)

    arr = list(np.random.randint(200, size=64))
    tic = time.perf_counter()
    count_flips(arr)
    toc = time.perf_counter()
    time1 = toc - tic
    flips.append(time1)
    print(toc-tic)

    arr = list(np.random.randint(200, size=128))
    tic = time.perf_counter()
    count_flips(arr)
    toc = time.perf_counter()
    time1 = toc - tic
    flips.append(time1)
    print(toc-tic)



if testTD1:
    # Test top down "magic stones" problem
    TDDS = []
    print("Testing Magical Stones Top Down with constant health, doubling stones")
    stones = [1]
    health = 800
    tic = time.perf_counter()
    magic_stones_topdown(stones, health)
    toc = time.perf_counter()
    time1 = toc - tic
    TDDS.append(time1)
    print(toc-tic)

    stones = [1, 4]
    tic = time.perf_counter()
    magic_stones_topdown(stones, health)
    toc = time.perf_counter()
    time1 = toc - tic
    TDDS.append(time1)
    print(toc-tic)

    # Test top down "magic stones" problem
    stones = [1, 4, 6, 11]
    tic = time.perf_counter()
    magic_stones_topdown(stones, health)
    toc = time.perf_counter()
    time1 = toc - tic
    TDDS.append(time1)
    print(toc-tic)

    # Test top down "magic stones" problem
    stones = [1, 4, 6, 7, 11, 15, 25, 30, 40]
    tic = time.perf_counter()
    magic_stones_topdown(stones, health)
    toc = time.perf_counter()
    time1 = toc - tic
    TDDS.append(time1)
    print(toc-tic)

    # Test top down "magic stones" problem
    stones = [1, 4,5, 6, 7, 11, 15,17 ,21, 24, 25,27, 30, 31,33,40]
    tic = time.perf_counter()
    magic_stones_topdown(stones, health)
    toc = time.perf_counter()
    time1 = toc - tic
    TDDS.append(time1)
    print(toc-tic)

    # Test top down "magic stones" problem
    stones = [1, 2, 3, 4,5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,
              18, 19, 20, 21, 22, 24, 25,27, 30,31 ,33,40, 41, 46, 48]
    tic = time.perf_counter()
    magic_stones_topdown(stones, health)
    toc = time.perf_counter()
    time1 = toc - tic
    TDDS.append(time1)
    print(toc-tic)

    # Test top down "magic stones" problem
    stones = np.arange(1,65)
    tic = time.perf_counter()
    magic_stones_topdown(stones, health)
    toc = time.perf_counter()
    time1 = toc - tic
    TDDS.append(time1)
    print(toc-tic)

    stones = np.arange(1,129)
    tic = time.perf_counter()
    magic_stones_topdown(stones, health)
    toc = time.perf_counter()
    time1 = toc - tic
    TDDS.append(time1)
    print(toc-tic)

if testBU1:
    # test bottom up
    BUDS =[]
    print("Magical Stones Bottom Up health constant, stones doubling")
    stones = [1]
    health = 800
    tic = time.perf_counter()
    magic_stones_bottomup(stones, health)
    toc = time.perf_counter()
    time1 = toc - tic
    BUDS.append(time1)
    print(toc-tic)

    stones = [1, 2]
    tic = time.perf_counter()
    magic_stones_bottomup(stones, health)
    toc = time.perf_counter()
    time1 = toc - tic
    BUDS.append(time1)
    print(toc-tic)

    stones = [1, 2, 3, 4]
    tic = time.perf_counter()
    magic_stones_bottomup(stones, health)
    toc = time.perf_counter()
    time1 = toc - tic
    BUDS.append(time1)
    print(toc-tic)

    stones = np.arange(1,9)
    tic = time.perf_counter()
    magic_stones_bottomup(stones, health)
    toc = time.perf_counter()
    time1 = toc - tic
    BUDS.append(time1)
    print(toc-tic)

    stones = np.arange(1,17)
    tic = time.perf_counter()
    magic_stones_bottomup(stones, health)
    toc = time.perf_counter()
    time1 = toc - tic
    BUDS.append(time1)
    print(toc-tic)

    stones = np.arange(1,32)
    tic = time.perf_counter()
    magic_stones_bottomup(stones, health)
    toc = time.perf_counter()
    time1 = toc - tic
    BUDS.append(time1)
    print(toc-tic)

    stones = np.arange(1,65)
    tic = time.perf_counter()
    magic_stones_bottomup(stones, health)
    toc = time.perf_counter()
    time1 = toc - tic
    BUDS.append(time1)
    print(toc-tic)

    stones = np.arange(1,129)
    tic = time.perf_counter()
    magic_stones_bottomup(stones, health)
    toc = time.perf_counter()
    time1 = toc - tic
    BUDS.append(time1)
    print(toc-tic)


# y = np.array([1,2,3,4,5,6,7,8])


plt.title("Magical Stones Top Down Constant Stones, Doubling Health Timing")
plt.xlabel("Size")
plt.ylabel("Time")
y = np.array(TDSC)
x = np.array(TDSChealth)
plt.plot(x,y,'o')
a,b = np.polyfit(x,y,1)
plt.plot(x,a*x+b)
# plt.loglog(x,a*x+b)
plt.show()

plt.title("Magical Stones Bottom Up Constant Stones, Doubling Health Timing")
plt.xlabel("Size")

plt.ylabel("Time")
y = np.array(BUSC)
x = np.array(TDSChealth)
plt.plot(x,y,'o')
a,b = np.polyfit(x,y,1)
plt.plot(x,a*x+b)

# plt.loglog(x,a*x+b)
plt.show()

plt.title("Magical Stones Top Down Constant Health, Doubling Stones Timing")
plt.xlabel("Size")
plt.ylabel("Time")
y = np.array(TDDS)
x = np.array([0,2,4,8,16,32,64,128])
plt.plot(x,y,'o')
a,b = np.polyfit(x,y,1)
plt.plot(x,a*x+b)
# plt.loglog(x,a*x+b)
plt.show()

plt.title("Magical Stones Bottom Up Constant Health, Doubling Stones Timing")
plt.xlabel("Size")
plt.ylabel("Time")

y = np.array(BUDS)
x = np.array([1,2,4,8,16,32,64,128])
plt.plot(x,y,'o')
a,b = np.polyfit(x,y,1)
plt.plot(x,a*x+b)
# plt.loglog(x,a*x+b)
plt.show()

plt.title("Flips Timing")
plt.xlabel("Size")
plt.ylabel("Time")
y = np.array(flips)
x = np.array([1,2,4,8,16,32,64,128])
plt.plot(x,y,'o')
a,b = np.polyfit(x,y,1)
plt.plot(x,a*x+b)
# plt.loglog(x,a*x+b)
plt.show()
