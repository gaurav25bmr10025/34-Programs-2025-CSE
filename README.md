# Number Theory & Integer Algorithms – Python Collection

This repository contains a curated collection of **34 Python programs** implementing classical and modern algorithms in:

- Number theory  
- Integer sequences  
- Modular arithmetic  
- Digital properties of numbers  

Each file is a standalone script and can be run from the command line.

---

## 📁 List of Programs

### 1–5: Arithmetic Functions (Assignments 1–5)

1. **`assignment_1.py` – Euler’s Totient Function φ(n)**  
   Computes the number of integers ≤ *n* that are coprime to *n*. Includes execution time and memory usage.

2. **`assignment_2.py` – Möbius Function μ(n)**  
   Implements the Möbius function based on prime factorization of *n*.

3. **`assignment_3.py` – Divisor Sum Function σ(n)**  
   Calculates the sum of all positive divisors of *n*.

4. **`ASSIGNMENT_4.py` – Prime Counting Function π(n)**  
   Counts how many primes are ≤ *n* using a simple primality test.

5. **`assignment_5.py` – Legendre Symbol (a/p)**  
   Computes the Legendre symbol \((a/p)\) and determines whether *a* is a quadratic residue modulo an odd prime *p*.

---

### 6–9: Advanced Number-Theoretic Functions

6. **`Integer Partition Function Calculator.py` – Partition Function p(n)**  
   Uses dynamic programming to compute the number of integer partitions of *n*.

7. **`Miller-Rabin Probabilistic Primality Test.py`**  
   Implements the Miller–Rabin primality test to check if a number is probably prime.

8. **`pollard.py` – Pollard’s Rho Factorization**  
   Uses Pollard’s Rho algorithm to find a non-trivial factor of a composite number.

9. **`Riemann Zeta Function Approximator.py`**  
   Approximates the Riemann zeta function ζ(s) using partial sums of the defining series.

---

### 10–14: Special Sequences & Properties (question26–30)

10. **`question26.py` – Lucas Sequence Generator**  
    Generates the first *n* terms of the Lucas sequence.

11. **`question27.py` – Perfect Power Checker**  
    Checks whether an integer *n* is a perfect power: \( n = a^b \) with integers \( a > 1, b > 1 \).

12. **`question28.py` – Collatz Length Calculator**  
    Computes the number of steps required for *n* to reach 1 under the Collatz (3n+1) iteration.

13. **`question29.py` – Polygonal Number Calculator**  
    Computes the *n*-th *s*-gonal number (triangular, square, pentagonal, etc. depending on *s*).

14. **`question30.py` – Carmichael Number Checker**  
    Uses Korselt’s criterion to check whether *n* is a Carmichael number.

---

### 15–19: Modular Arithmetic & Primality Tools

15. **`chinese remainder theorm.py` – Chinese Remainder Theorem Solver**  
    Solves systems of congruences using CRT and modular inverses.

16. **`Fibonacci Prime Checker.py`**  
    Checks whether a number is both Fibonacci and prime (a Fibonacci prime).

17. **`Modular Multiplicative Inverse Finder.py`**  
    Uses the extended Euclidean algorithm to compute the modular inverse of *a* modulo *m* (if it exists).

18. **`Order Modulo Finder.py`**  
    Computes the multiplicative order of *a* modulo *n*, i.e. the smallest *k* such that \( a^k ≡ 1 \pmod{n} \).

19. **`QuadraticResidue_Checker.py` – Quadratic Residue Test**  
    Determines whether *a* is a quadratic residue modulo *p* using Euler’s criterion.

---

### 20–28: Divisors, Special Numbers, and Prime Variants

20. **`Aliquot Sum Calculator.py`**  
    Computes the aliquot sum of *n* (sum of proper divisors, excluding *n* itself).

21. **`Amicable Numbers Checker.py`**  
    Checks whether two numbers form an amicable pair using their aliquot sums.

22. **`Highly Composite Number Checker.py`**  
    Determines if *n* is highly composite by comparing its number of divisors with all smaller positive integers.

23. **`Multiplicative Persistence Counter.py`**  
    Repeatedly multiplies the digits of *n* and counts how many steps it takes to reach a single-digit number (multiplicative persistence).

24. **`Check if Number is Prime Power.py`**  
    Checks whether *n* is a prime power \( p^k \) for some prime *p* and integer *k > 1*.

25. **`Count Distinct Prime Factors.py`**  
    Counts how many **distinct** prime factors *n* has.

26. **`Mersenne Prime Checker.py`**  
    Given an integer *p*, checks whether \( 2^p - 1 \) is a Mersenne prime.

27. **`Number of Divisors Counter.py`**  
    Counts the total number of positive divisors of *n*.

28. **`Twin Primes Generator.py`**  
    Uses the Sieve of Eratosthenes to generate all twin prime pairs up to a given limit.

---

### 29–33: Digit-Based & Basic Arithmetic Programs

29. **`q3_assignment3.py` – Mean of Digits**  
    Computes the arithmetic mean of the decimal digits of an integer *n*.

30. **`q4_assignment4.py` – Digital Root Calculator**  
    Repeatedly sums the digits of *n* until a single-digit result is obtained (digital root).

31. **`question_2.py` – Palindrome Number Checker with Timing/Memory**  
    Reverses the digits of *n*, checks if it is a palindrome, and measures execution time and memory usage.

32. **`question1_assignment2.py` – Factorial Calculator**  
    Computes *n!* iteratively.

33. **`q5_assignment2.py` – Abundant Number Checker**  
    Determines whether *n* is an abundant number (sum of proper divisors > *n*).

---

### 34: Modular Exponentiation

34. **`Modular Exponentiation Function.pyt` – Fast Power Modulo (file)**  
    This file appears to implement modular exponentiation (fast power modulo).  
    > 💡 Tip: for consistency, you may want to rename this to `Modular Exponentiation Function.py` before pushing to GitHub.

---

## 🧪 How to Run the Programs

All scripts are standard Python files. From the repository root, run:

```bash
python filename.py
