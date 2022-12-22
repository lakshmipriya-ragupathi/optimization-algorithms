import math

def f(x):
    return pow(((pow((x / 2), 2) / 3456) + 3), 2)


def fun1(x):
    return ((x - 56) / 31) * math.exp((x + 42) / 34) * math.exp(-((x + 23) / 24)) + 34


def fun2(x):
    return -(pow(((x - 3) / 43), 4) / 64) + 27 * (x - 31)


def fun3(x):
    return (-x - 56) / 31 - math.exp((-x + 42) / 34) - math.exp((x + 23) / 124) + 245


def nearestFibonacci(num):  # Will return the nearest Fibo number
    if num == 0:
        print(0)
        return
    first = 0
    second = 1
    third = first + second
    while third <= num:
        first = second
        second = third
        third = first + second
    if abs(third - num) >= abs(second - num):
        ans = second
    else:
        ans = third
    return ans


def findIndex(n):  # Finds the position of the fibonacci number
    if n <= 1:
        return n
    a, b, c, res = 0, 1, 1, 1
    while c < n:
        c = a + b
        res = res + 1
        a = b
        b = c
    return res


def fibonn(x):
    if x == 0:
        return 1
    elif x == 1:
        return 1
    else:
        a, b = 1, 1
        c = 0
        for i in range(1, x):
            c = a + b
            a = b
            b = c
        return c


a = -1500
b = 1500
tol = 0.001
n = findIndex(nearestFibonacci((2 * (b-a))/tol))
k = 2
L = b - a

s = (1 - math.sqrt(5)) / (1 + math.sqrt(5))
phi = (1 + math.sqrt(5)) / 2
rho = 1 / (phi * (1 - s ** (n + 1)) / (1 - s ** n))
d = rho * b + (1 - rho) * a
yd = f(d)
for i in range(1, n - 1):
    if i == n - 1:
        c = tol * a + (1 - tol) * d
    else:
        c = rho * a + (1 - rho) * b

    yc = f(c)
    if yc < yd:
        b, d, yd = d, c, yc
    else:
        a, b = b, c

    rho = 1 / (phi * (1 - s ** (n - i + 1)) / (1 - s ** (n - i)))

    print(a, b)
