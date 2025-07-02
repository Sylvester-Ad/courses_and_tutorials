import sympy as sp


def bisection(f, a, b, number_of_iterations):
    """
    Purpose: Function to find the root of a function using the bisection method
    """
    # Validate the interval
    if (f(a) * f(b) >= 0):
        return f"Invalid interval. {a} and {b} do not contain the root."

    i = 0
    c = 0

    while i < number_of_iterations:  # or f(c) != 0:
        c = (a + b) / 2

        print(f"Root c({i}): {round(c, 5)} (found in {i} iterations)")
        if f(c) == 0:
            break
        if f(a) * f(c) < 0:
            b = c
        elif f(b) * f(c) < 0:
            a = c

        i += 1

    return f"Root: {round(c, 4)} (found in {i} iterations)."


# Ask for function
user_input = input("Enter a function in terms of x(Enter 'E' for euler's): ")

# Get number of iterations and the initial point
a = float(input("Enter your initial point (a): "))
b = float(input("Enter your initial point (b): "))
number_of_iterations = float(input("Enter the number of iterations: "))

# Symbol
x = sp.symbols('x')

# Parse the expression
expr = sp.sympify(user_input)

# Convert to Python function
f = sp.lambdify(x, expr)


result = bisection(f, a, b, number_of_iterations)
print(result)
