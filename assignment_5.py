import time
import tracemalloc

def legendre_symbol(a: int, p: int) -> int:
    if p <= 2:
        raise ValueError("p must be an odd prime.")
    a = a % p  
    if a == 0:
        return 0  
    result = pow(a, (p - 1) // 2, p)
    if result == p - 1:  
        return -1
    else:
        return result

# --- Main Execution ---
if __name__ == "__main__":
    a = int(input("Enter integer a: "))
    p = int(input("Enter an odd prime p: "))

    tracemalloc.start()
    start_time = time.perf_counter()

    result = legendre_symbol(a, p)

    end_time = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Legendre symbol ({a}/{p}) = {result}")
    print(f"Execution Time: {end_time - start_time:.12f} seconds")
    print(f"Memory Utilization: {peak} bytes")