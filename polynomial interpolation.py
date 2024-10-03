import matplotlib as plt
from sympy import symbols


def l_func(x_values, x, degree):
    l = 1
    x = symbols("x")
    for i in range(degree + 1):
        for k in range(degree + 1):
            if i != k:
                l *= (x - x[i]) / (x[k] - x[i])  # Calculation of L parameters
    return l


def polynomial_interpolation(x, y, degree):
    p = 0
    for x in range(degree + 1):
        p += y[x] * l_func(x, x, degree) # Polynomial Calculation
    return p


def graph_plot(x, y, p, degree):
    plt.plot(polynomial_interpolation(x, y, degree))
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Polynomial Interpolation")
    plt.show()

def main():
    x = []
    y = []
    n = int(input("> "))
    # get x y data from user
    for z in range(n + 1):
        xi = int(input(f"Insert x value: "))
        yi = int(input(f"Insert y value: "))
        x.append(xi)
        y.append(yi)
    polynomial_interpolation(x, y, n)


main()


