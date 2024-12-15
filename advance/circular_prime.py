import itertools

def is_prime(n):
    if n < 2:
        return False

    r = int(n**0.5) + 1
    for i in range(2, r):
        if n % i == 0:
            return False

    return True

def gen_circularPrime(n1, n2):
    count = 0
    while n1 < n2:
        if is_prime(n1):
            # Generate all unique permutations of the number
            permutations = set(int(''.join(p)) for p in itertools.permutations(str(n1)))
            
            # Check if all permutations are prime
            if all(is_prime(num) for num in permutations):
                count += len(permutations)
                yield n1  # Yield the number once
        n1 += 1
    # print("Total permutations checked:", count)
    # # return count

cPrime = gen_circularPrime(2, 1000000)
count = 0
for prime in cPrime:
    count += 1
    print(prime, end=' ')

print(count)

# gen_circularPrime(2, 1000000)