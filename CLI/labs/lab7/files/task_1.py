from numpy import *
import matplotlib.pyplot as plt

def f(x):
    return 5*sin(10*x)*sin(3*x)
x = linspace(0, 4, 400)
y = f(x)
plt.plot(x, y)
plt.savefig("function_sin.png")
plt.show()