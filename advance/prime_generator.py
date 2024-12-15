def is_prime(n):
    if n < 2:
        return False

    r = int(n**0.5) + 1
    for i in range(2, r):
        if n % i == 0:
            return False

    return True

def gen_prime():
    num = 2  # Start from the first prime number
    count = 0
    while count < 100:
        if is_prime(num):
            yield num
            count += 1
        num += 1

# Generate and print the first 100 primes
primes = gen_prime()
for prime in primes:
    print(prime, end=' ')
print("######################################")

# Generate and print the first 100 primes second approach 
p = gen_prime()
for i in range(100):
    print(next(p), end=' ')
