import matplotlib
from sympy import symbols

data_set = []

def polynomial_interpolation(y):
    x = symbols("x")
    p = 0
    for z in range(y):
        xi = int(input(f"Insert x value: "))
        yi = int(input(f"Insert y value: "))
        data_set.append((xi, yi))
    x_values = [x for x, y in data_set]
    for c in range(y):
        p = p + x_values[c]


def main():
    n = int(input("> "))
    polynomial_interpolation(n)

main()

