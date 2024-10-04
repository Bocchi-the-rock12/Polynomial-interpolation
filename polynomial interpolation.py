import matplotlib.pyplot as plt
from sympy import symbols, simplify
from numpy import linspace


def l_func(x_values, k, n):
    l = 1
    x = symbols("x")
    for i in range(n + 1):
        if i != k:
            # Only one loop because the second parameter of the products comes from the sum
            l *= (x - x_values[i]) / (x_values[k] - x_values[i])  # Calculation of L parameters
    return l


def polynomial_interpolation(x_var, y, z):
    p = 0
    for k in range(z + 1):
        p += y[k] * l_func(x_var, k, z) # Polynomial Calculation
    return p


def graph_plot(x, y, p, f):
    plt.figure(figsize=(11, 8))
    manager = plt.get_current_fig_manager()
    manager.window.title("Lagrange Polynomial Interpolation")
    plt.xlabel("X-axis", fontsize=12)
    plt.ylabel("Y-axis", fontsize=12)
    plt.title("Polynomial Interpolation", fontsize=16, fontweight="bold")
    plt.xlim(min(x), max(x))
    plt.ylim(min(y), max(y))
    plt.axhline(0, color="black", linewidth=2, ls="-")
    plt.axvline(0, color="black", linewidth=2, ls="-")
    x_values = linspace(min(x), max(x), 1000)
    y_values = [polynomial_interpolation(x, y, f).subs("x", val) for val in x_values]
    y_values = [float(val) for val in y_values]
    plt.plot(x_values, y_values)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()


def main():
    x_data_set = []
    y_data_set = []
    n = int(input("Insert the degree of your polynomial: "))
    # get x, y data from user
    for z in range(n + 1):
        xi = int(input(f"Insert x value: "))
        yi = int(input(f"Insert y value: "))
        x_data_set.append(xi)
        y_data_set.append(yi)
    graph_plot(x_data_set, y_data_set, simplify(polynomial_interpolation(x_data_set, y_data_set ,n)), n)

main()


