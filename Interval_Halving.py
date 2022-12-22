import time
from math import *
start_time=time.time()
def f(x):
    return pow(((pow((x/2),2)/3456)+3),2)
def fun1(x):
    return ((x-56)/31)*exp((x+42)/34)*exp(-((x+23)/24))+34
def fun2(x):
    return -(pow(((x-3)/43),4)/64)+27*(x-31)
def fun3(x):
    return (-x-56)/31-exp((-x+42)/34)-exp((x+23)/124)+245


a, b, tolerance = -1500, 1500, 0.001
e = 0.001

search_region = (a, b)

number_of_intervals = floor(2*log((tolerance/(b-a)), 0.5))
for i in range(number_of_intervals):
    Xm = (a + b)/ 2
    X1 = Xm - e
    X2 = Xm + e

    if f(X1) < f(Xm):
        b = Xm

    elif f(X2) < f(Xm):
        a = Xm

    else:
        a = X1
        b = X2
end_time=time.time()
print("Time taken for execution: ",end_time-start_time)
print(a, b)