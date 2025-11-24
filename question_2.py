import time 
import tracemalloc


def reversenumber(num):
    rn = 0
    while num > 0:
        rn = rn * 10 + num % 10
        num = num // 10
    return rn

n = int(input("Enter a number:"))

tracemalloc.start()
start_time = time.perf_counter()


if reversenumber(n) == n:
    print("palindrome")
else:
    print("not a palindrome")


end_time = time.perf_counter()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()



print(f"Execution Time: {end_time - start_time:.12f} seconds")
print(f"Memory Utilization: {peak} bytes")   
