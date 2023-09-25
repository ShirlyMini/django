import time
from concurrent.futures import ThreadPoolExecutor


def cube(x):
    #return (f"cube of {x} is {x * x * x}")
    print(f"cube of {x} is {x * x * x}")
    time.sleep(3)

with ThreadPoolExecutor(max_workers=2) as ex:
    ex.submit(cube, 2)

    #results = ex.map(cube, [2,3,4,5,6])

    # for r in results:
    #     print(r)
    #

