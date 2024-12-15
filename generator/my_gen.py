def my_gen(start=0,step=1,last=10):
    num = start
    while num < last:
        yield num
        num += step


gen = my_gen(20,3,50)
for num in gen:
    print(num)