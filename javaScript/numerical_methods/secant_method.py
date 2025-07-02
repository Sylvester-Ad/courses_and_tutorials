import sympy as sp


def secant_method(f, x0, x1, tolerance=1e-7, max_iter=100):
    """
    Function to find a root using the Secant method.

    Parameters:
        f        - the function (callable)
        x0, x1   - initial guesses
        tolerance - convergence threshold (default: 1e-7)
        max_iter  - max number of iterations (default: 100)
    """
    for i in range(2, max_iter + 2):
        f_x0 = f(x0)
        f_x1 = f(x1)
        denominator = f_x1 - f_x0

        if denominator == 0:
            raise ZeroDivisionError(f"Zero division at iteration {i}: f(x1) - f(x0) = 0")

        x_next = x1 - (f_x1 * (x1 - x0)) / denominator
        print(f"x({i}) = {round(x_next, 5)}")

        if abs(x_next - x1) < tolerance:
            return f"\nConverged to root: {round(x_next, 5)} in {i - 2} iterations"

        x0, x1 = x1, x_next

    return f"\nFunction did not converge after {max_iter} iterations. Last value: x = {round(x_next, 5)}"


# Input from user
user_input = input("Enter a function in terms of x (use 'e' for Euler's constant, e.g., x**2 - e**x): ")

# Define symbol
x = sp.symbols('x')

# Define allowed constants/functions for safe parsing
allowed = {
    'e': sp.E,
    'pi': sp.pi,
    'sin': sp.sin,
    'cos': sp.cos,
    'tan': sp.tan,
    'log': sp.log,
    'ln': sp.ln,
    'exp': sp.exp,
    'sqrt': sp.sqrt
}

# Parse expression
expr = sp.sympify(user_input, locals=allowed)

# Convert to Python function
f = sp.lambdify(x, expr)

# Initial guesses
x0 = float(input("Enter first guess (x0): "))
x1 = float(input("Enter second guess (x1): "))

# Run Secant Method
result = secant_method(f, x0, x1, tolerance=10**-7)
print(result)
