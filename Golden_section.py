import math
import time
start_time=time.time()
# phi is the golden ratio
invphi = (math.sqrt(5) - 1) / 2  # 1 / phi
invphi2 = (3 - math.sqrt(5)) / 2  # 1 / phi^2

def f(x):
    return pow(((pow((x/2),2)/3456)+3),2)
def fun1(x):
    return ((x-56)/31)*math.exp((x+42)/34)*math.exp(-((x+23)/24))+34
def fun2(x):
    return -(pow(((x-3)/43),4)/64)+27*(x-31)
def fun3(x):
    return (-x-56)/31-math.exp((-x+42)/34)-math.exp((x+23)/124)+245


a = -1500
b = 1500

tolerance = 0.001 # tolerance is epsilon


def gss(f, a, b, tol):
    (a, b) = (min(a, b), max(a, b))
    h = b - a
    if h <= tol:
        return (a, b)

    number_of_steps = int(math.ceil(math.log(tol / h) / math.log(invphi)))

    c = a + invphi2 * h
    d = a + invphi * h
    c_f = f(c)
    d_f = f(d)

    for k in range(number_of_steps - 1):
        if c_f < d_f:  # yc > yd to find the maximum
            b = d
            d = c
            d_f = c_f
            h = invphi * h
            c = a + invphi2 * h
            c_f = f(c)
        else:
            a = c
            c = d
            c_f = d_f
            h = invphi * h
            d = a + invphi * h
            d_f = f(d)

    if c_f < d_f:
        return (a, d, number_of_steps)
    else:
        return (c, b, number_of_steps)


print(gss(f, a, b, tolerance))
end_time=time.time()
print("Time taken for execution: ",end_time-start_time)