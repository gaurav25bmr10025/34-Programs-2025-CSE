import time
import tracemalloc

def divisor_sum(n: int) -> int:
    total = 0
    for i in range(1, n + 1):
        if n % i == 0:
            total += i
    return total

# --- Main Execution ---
if __name__ == "__main__":
    n = int(input("Enter a positive integer n: "))

    tracemalloc.start()
    start_time = time.perf_counter()

    result = divisor_sum(n)

    end_time = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"o({n}) = {result}")
    print(f"Execution Time: {end_time - start_time:.12f} seconds")
    print(f"Memory Utilization: {peak} bytes")