def fib(n):
    a, b = 0, 1
    while n > 0:
        yield a
        a, b = b, a + b
        n -= 1

fib_gen = fib(10)
print(f"{fib_gen=}")

for i in fib_gen:
    print(i)
