import time
import tracemalloc

def is_prime(x: int) -> bool:
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    i = 3
    while i * i <= x:
        if x % i == 0:
            return False
        i += 2
    return True

def prime_pi(n: int) -> int:
    count = 0
    for i in range(2, n + 1):
        if is_prime(i):
            count += 1
    return count

# --- Main execution ---
if __name__ == "__main__":
    n = int(input("Enter a positive integer n: "))

    tracemalloc.start()
    start_time = time.perf_counter()

    result = prime_pi(n)

    end_time = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"π({n}) = {result}")
    print(f"Execution Time: {end_time - start_time:.12f} seconds")
    print(f"Memory Utilization: {peak} bytes")