# from math import 
from numpy import linspace, sin, cos, pi
import matplotlib.pyplot as plt

x = linspace(-2*pi,2*pi,500)
cosx = cos(x)
sinx = sin(x)

plt.plot(x,sinx,label="sin(x)")
plt.plot(x,cosx,label="cos(x)")
plt.title("sin(x) and cos(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.savefig("sine_plot.png")