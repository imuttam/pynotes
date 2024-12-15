def is_prime(n):
    if n < 2:
        return False

    r = int(n**0.5) + 1
    for i in range(2, r):
        if n % i == 0:
            return False

    return True

def gen_prime_length():
    num = 2  # Start from the first prime number
    count = 0
    sum_prime = 0
    sum_lst = []
    while count < 100:
        if is_prime(num):
            sum_prime += num
            if is_prime(sum_prime):
                sum_lst.append(num)
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
