import numpy as np

def derivate3(func, x, epsilon):
    # three point method 
    return (func(x+epsilon) - func(x-epsilon)) /(2 * epsilon)

def derivate2(func, x, epsilon):
    return (func(x+epsilon) - func(x)) / epsilon


def derivate_3pm(func, mini, maxi, epsilon):
    int_range = np.linspace(mini, maxi, 100)
    derivations = []

    for i in int_range:
        derivations.append(derivate3(func, i, epsilon))

    return derivations


def derivate_3pmm(func, mini, maxi, epsilon):
    int_range = np.linspace(mini, maxi, 100)
    derivations = []

    for i in int_range:
        derivations.append(derivate3(func, i, epsilon))

    return int_range


def derivate_2pm(func, mini, maxi, epsilon):
    int_range = np.linspace(mini, maxi, 100)
    derivations = []

    for i in int_range:
        derivations.append(derivate2(f1, i, epsilon))

    return derivations, int_range