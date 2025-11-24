import time
import tracemalloc

def mobius(n: int) -> int:
    if n == 1:
        return 1   
    
    prime_factors = {}
    i = 2
    temp = n 
    
    while i * i <= temp:
        count = 0
        while temp % i == 0:
            temp //= i
            count += 1
        if count > 1:
            return 0  # squared prime factor found
        if count == 1:
            prime_factors[i] = 1
        i += 1 
    
    if temp > 1:  
        prime_factors[temp] = 1

    # check number of distinct primes
    if len(prime_factors) % 2 == 0:
        return 1
    else:
        return -1


# --- Main Execution ---
if __name__ == "__main__":
    n = int(input("Enter a positive integer n: "))

    tracemalloc.start()
    start_time = time.perf_counter()

    result = mobius(n)

    end_time = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"μ({n}) = {result}")
    print(f"Execution Time: {end_time - start_time:.12f} seconds")
    print(f"Memory Utilization: {peak} bytes")