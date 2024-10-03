import matplotlib
from sympy import symbols

def polynomial_interpolation(x_values, y_values, degree):
    p = 0
    for x in range(degree + 1):
        p += y_values[x] * l_func(x_values, x, degree) # Polynomial Calculation
    print(p)


def l_func(x_values, x, degree):
    l = 1
    x = symbols("x")
    for i in range(degree + 1):
        for k in range(degree + 1):
            if i != k:
                l *= (x - x_values[k]) / (x_values[i] - x_values[k])  # Calculation of L parameters
    return l


def plot_graph(f):
    print("ola")


def main():
    n = int(input("> "))
    # get x y from user input
    data_set = []
    for z in range(n + 1):
        xi = int(input(f"Insert x value: "))
        yi = int(input(f"Insert y value: "))
        data_set.append((xi, yi))
    x_values = [x for x, y in data_set]  # List of x values
    y_values = [y for x, y in data_set]  # List of y values
    polynomial_interpolation(x_values, y_values, n)

main()

