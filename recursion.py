n = int(input("Enter a number: "))
i = 0
for a in range(n + 1):
    i = a + i
print(i)

# recursion
def sum(n):
    if n == 1:
        return 1
    else:
        return n + sum(n - 1)

print(sum(n))

#recursion for fibbonacci series
def series(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return series(n-2) + series(n-1)
print(series(n))