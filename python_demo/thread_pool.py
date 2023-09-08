from concurrent.futures import ThreadPoolExecutor
import time

def thread_fucn(num):
    print(f"Start thread {num}")
    time.sleep(3)
    print(f"End thread {num}")

def thread_fucn2(num):
    print(f"Start thread {num*11}")
    time.sleep(3)
    print(f"End thread {num*11}")

with ThreadPoolExecutor(max_workers=12) as exe:
    exe.map(thread_fucn, [1,2,3,4,5,6])
    exe.map(thread_fucn2, [1,2,3,4,5,6])

    # exe.submit(thread_fucn,1)
    # exe.submit(thread_fucn,2)
    # exe.submit(thread_fucn,3)
    # exe.submit(thread_fucn,4)
    # exe.submit(thread_fucn,5)
    # exe.submit(thread_fucn,6)
    # exe.submit(thread_fucn,7)
    # exe.submit(thread_fucn,8)