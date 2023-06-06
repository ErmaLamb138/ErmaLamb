import numpy as np

def prime_numbers(n):
    primes = []
    for i in range(2, n+1):
        is_prime = True
        for j in range(2, int(np.sqrt(i))+1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes

def fibonacci_sequence(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

def calculate_pi(n):
    pi_sum = 0.0
    for i in range(n):
        term = (-1)**i / (2*i + 1)
        pi_sum += term
    return 4 * pi_sum

def main():
    n = 100
    primes = prime_numbers(n)
    fib = fibonacci_sequence(n)
    pi_approx = calculate_pi(n)
    print("Prime numbers up to", n, ":", primes)
    print("Fibonacci sequence up to", n, ":", fib)
    print("Approximation of pi using", n, "terms:", pi_approx)

if __name__ == '__main__':
    main()
