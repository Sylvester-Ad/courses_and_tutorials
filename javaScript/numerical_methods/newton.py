import sympy as sp

# Define the symbol
x_symbol = sp.Symbol('x')


def newton(expr, x0, number_of_iterations):
    """
    Implements the Newton-Raphson method to find the root of a given mathematical expression.

    Parameters:
        expr (str): The mathematical expression as a string. 
                    Example: "x**2 - 4" or "sin(x) - x/2".
        x0 (float): The initial guess for the root.
        x1 (float): The initial guess for the root.
        number_of_iterations (int): The maximum number of iterations to perform.
    """

    x = x0
    i = 0

    # Define safe functions/constants for parsing
    allowed = {
        'pi': sp.pi,
        'sin': sp.sin,
        'cos': sp.cos,
        'tan': sp.tan,
        'ln': sp.ln,
        'log': sp.log,
        'exp': sp.exp,
        'sqrt': sp.sqrt
    }

    # Parse the expression safely
    expr = sp.sympify(expr, locals=allowed)

    # Create function and derivative
    f = sp.lambdify(x_symbol, expr)
    f_prime_expr = sp.diff(expr, x_symbol)
    f_prime = sp.lambdify(x_symbol, f_prime_expr)

    while i < number_of_iterations:
        x_next = x - (f(x) / f_prime(x))
        print(f"x({i}) = {round(x_next, 5)}")

        if abs(x_next - x) < 1e-5:
            return f"\nConverged to root: {round(x_next, 5)} in {i} iterations"
        
        x = x_next
        i += 1

    return f"\nFunction was unable to converge. Ended in {i} iterations (x = {round(x, 5)})."


# --- Input Section ---
user_input = input("Enter a function in terms of x (e.g., 'x**2 - e**x'): ")
initial_point = float(input("Enter your initial point: "))

# Run Newton's method
result = newton(expr=user_input, x0=initial_point, number_of_iterations=100)
print(result)

