x = 100
def f1():
    x = 88
    def f2():
        print(x)
    return f2

action = f1()
print(action)
action()