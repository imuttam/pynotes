# gen_exp = (x*x for x in range(20) if x % 2 != 0)
# 
# total = 0
# for square in gen_exp:
#     print(square)  # Print each value from the generator
#     total += square
#     print(f"Total so far: {total}")

def square_generator():
    gen_exp = (x*x for x in range(20) if x % 2 != 0)
    total = 0
    for square in gen_exp:
        yield square  # Yield the value instead of printing
        total += square
        print(f"Total so far: {total}")

# Example of how to use the generator function
for value in square_generator():
    print(f"Generated value: {value}")

    

