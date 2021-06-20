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


def integrate_rectangle(func, a, b, n):
    h = (b-a)/n
    upper = 0
    lower = 0
    i = a
    j = a + h
    for k in range(n):
        if abs(func(i)) >= abs(func(j)):
            upper += func(i)*h
            lower += func(j)*h
        else:
            upper += func(j)*h
            lower += func(i)*h
        i += h
        j += h

    return lower, upper

def integrate_trapezoid(func, a, b, n):
    h = (b-a) / n
    integral = 0
    i = a
    j = a + h

    for k in range(n):
        integral += ((func(i) + func(j))/2)*h
        i += h
        j += h

    return integral

