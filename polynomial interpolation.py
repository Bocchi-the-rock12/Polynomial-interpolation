import matplotlib
from sympy import symbols

def polynomial_interpolation(degree):
    data_set = []
    L = [1] * (degree + 1)
    x = symbols("x")
    p = 0 # Lagrange Polynomial of n degree
    for z in range(degree + 1):
        xi = int(input(f"Insert x value: "))
        yi = int(input(f"Insert y value: "))
        data_set.append((xi, yi))
    x_values = [x for x, y in data_set] # List of x values
    y_values = [y for x, y in data_set] # List of y values
    for i in range(0, degree + 1):
        for k in range(0, degree + 1):
            if i != k:
                L[i] = L[i] * (x - x_values[k]) / (x_values[i] - x_values[k]) # Calculation of L parameters
    for x in range(degree + 1):
        p = p + (y_values[x] * L[x]) # Polynomial Calculation
    print(p)


def main():
    n = int(input("> "))
    polynomial_interpolation(n)

main()

