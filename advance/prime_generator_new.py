def is_prime(n):
    if n < 2:
        return False

    r = int(n**0.5) + 1
    for i in range(2, r):
        if n % i == 0:
            return False

    return True

def gen_prime(start, stop):

    while start < stop:
        if is_prime(start):
            yield start
        start += 1

# Generate and print the first 100 primes
primes = gen_prime(6000, 8000)
for prime in primes:
    print(prime, end=' ')


# # Generate and print the first 100 primes second approach 
# p = gen_prime()
# for i in range(100):
#     print(next(p), end=' ')
