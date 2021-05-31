import numpy as np

def derivate3(func, x, epsilon):
    # three point method 
    return (func(x+epsilon) - func(x-epsilon)) /(2 * epsilon)


def derivate2(func, x, epsilon):
    return (func(x+epsilon) - func(x)) / epsilon


def derivate_3pm(func, mini, maxi, epsilon):
    step_number = int(1/epsilon)
    int_range = np.linspace(mini, maxi, step_number)
    derivations = []

    for i in int_range:
        derivations.append(derivate3(func, i, epsilon))

    return derivations, int_range


def derivate_2pm(func, mini, maxi, epsilon):
    step_number = int(1/epsilon)
    int_range = np.linspace(mini, maxi, step_number)
    derivations = []

    for i in int_range:
        derivations.append(derivate2(func, i, epsilon))

    return derivations, int_range


def integrate_rectangle(func, mini, maxi, steps):
    lower_list = []
    upper_list = []
    dx = (abs(maxi - mini)) / steps
    values = []

    for i in range(steps+1):
        values.append(func(i*dx)*dx)

    for j in values:
        lower_list.append(j)
        upper_list.append(j)

    del lower_list[-1]
    del upper_list[0]
    lower = sum(values[0:-1])
    upper = sum(values[1:])

    return lower, upper, sum(values)

def integrate_trapezoid(func, mini, maxi, steps):
    dx = (abs(maxi - mini)) / steps
    values = [] 

    for i in range(steps+1):
        values.append((func(i*dx) + func((i+1)*dx)))

    value = (sum(values)*dx) / 2

    return value

def integrate_upper_lower(func, mini, maxi, steps):
    dx = (abs(maxi - mini)) / steps
    up = 0
    down = 0
    for i in range(0, steps):
        up += func((i+1)*dx)*dx
        down += func(i*dx)*dx
        
    return up, down

