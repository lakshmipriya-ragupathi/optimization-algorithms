import math
import time

start_time = time.time()


def f(x):
    return pow(((pow((x / 2), 2) / 3456) + 3), 2)


def fun1(x):
    return ((x - 56) / 31) * math.exp((x + 42) / 34) * math.exp(-((x + 23) / 24)) + 34


def fun2(x):
    return -(pow(((x - 3) / 43), 4) / 64) + 27 * (x - 31)


def fun3(x):
    return (-x - 56) / 31 - math.exp((-x + 42) / 34) - math.exp((x + 23) / 124) + 245


a, b, tolerance = -1500, 1500, 0.001

search_region = (a, b)
bracketed_region = 0

number_of_intervals = ((b - a) // tolerance) + 1

Xo = a
X1 = a + tolerance
X2 = X1 + tolerance

Xo_f = f(Xo)
X1_f = f(X1)
X2_f = f(X2)

while X2 < b:
    if Xo_f >= X1_f <= X2_f:
        bracketed_region = (Xo, X2)
        break
    else:
        Xo = X1
        X1 = X2
        X2 += tolerance
        Xo_f = X1_f
        X1_f = X2_f
        X2_f = f(X2)

print(bracketed_region)
end_time = time.time()
print("Time taken for execution: ", end_time - start_time)
