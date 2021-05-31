import calculus as cal
import matplotlib.pyplot as plt
import numpy as np

def cubic(x):

    return x**3

def cubic_integrate(x):
    
    return (x**4)/4

steps = 1000
step_range = np.arange(0, steps+10, 50)
lower, upper, num_rectangle_value = cal.integrate_rectangle(cubic, 0, 5, steps)
num_trapezoid_value = cal.integrate_trapezoid(cubic, 0, 5, steps)
upper_List, lower_list = cal.integrate_upper_lower(cubic, 0, 5, steps)
num_rectangle_values = []
num_trapezoid_values = []
lower = [] 
upper = []
analytical_values = []

for i in step_range:

    lower, upper, num_rectangle_value = cal.integrate_rectangle(cubic, 0, 5, i)
    num_rectangle_values.append(num_rectangle_value)

    num_trapezoid_values.append(cal.integrate_trapezoid(cubic, 0, 5, i))

    analytical_values.append(cubic_integrate(5))

# plt.plot(step_range, analytical_values, label="analytical result") # analytical
# plt.scatter(step_range, num_trapezoid_values, label="numerical-trapezoid result") # numerical-trapezoid
# plt.scatter(step_range, num_rectangle_values, label="numerical-rectangle result") # numerical-rectangle
# plt.legend()
# plt.xlabel("Number of steps")
# plt.ylabel("Integral value")
# plt.show()
plt.plot(step_range, analytical_values, label="analytical result") # analytical
plt.scatter(step_range, lower, label="numerical-trapezoid result") # numerical-trapezoid
plt.scatter(step_range, upper, label="numerical-rectangle result") # numerical-rectangle
plt.legend()
plt.xlabel("Number of steps")
plt.ylabel("Integral value")
plt.show()

