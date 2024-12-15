def maker(n):
    def action(x):
        return x**n
    return action

f = maker(2)
for i in range(10):
    print(f(i), end= ' ')