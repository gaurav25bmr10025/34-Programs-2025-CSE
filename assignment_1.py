import math
import time
import tracemalloc

def euler_phi(n: int) -> int:
    count = 0
    for i in range(1, n + 1):
        if math.gcd(i, n) == 1:
            count += 1
    return count

if __name__ == "__main__":
    n = int(input("Enter a number: "))

    tracemalloc.start()
    start_time = time.perf_counter()  

    result = euler_phi(n)

    end_time = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"φ({n}) = {result}")
    print(f"Execution Time: {end_time - start_time:.12f} seconds")
    print(f"Memory Utilization: {peak} bytes")