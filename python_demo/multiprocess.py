import math
import multiprocessing
import time

sqrt4 = []
sqrt5 = []
sqrt6 = []


def sqrtof4(num):
    for i in num:
        sqrt4.append(math.sqrt(i ** 4))


def sqrtof5(num):
    for i in num:
        sqrt5.append(math.sqrt(i ** 5))


def sqrtof6(num):
    for i in num:
        sqrt6.append(math.sqrt(i ** 6))


if __name__ == "__main__":
    number_list= list(range(5000000))

    start=time.time()
    sqrtof4(number_list)
    sqrtof5(number_list)
    sqrtof6(number_list)
    end=time.time()
    print(end-start)

    start = time.time()
    p1=multiprocessing.Process(target=sqrtof4, args=[number_list])
    p2=multiprocessing.Process(target=sqrtof5, args=[number_list])
    p3=multiprocessing.Process(target=sqrtof6, args=[number_list])
    p1.start()
    p2.start()
    p3.start()
    end = time.time()
    print(end - start)



