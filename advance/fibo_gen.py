def gen_fibo():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Use the generator to print the first 100 Fibonacci numbers
total = 0
fib = gen_fibo()
for i in range(100):
    print(next(fib), end=' ')
    # total+= next(fib)

print()

"""Second way to generate 100 fibs"""

def fibo_100():
    a, b = 0, 1
    count = 0
    while count < 100:
        yield a
        count += 1
        a, b = b, a + b

fib_gen = fibo_100()
for f in fib_gen:
    print(f, end=' ')
