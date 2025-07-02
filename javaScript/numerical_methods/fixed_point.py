import math


def fixed_point_iteration(g, x0, tolerance=1e-6, max_iterations=100):
    """
    Finds the root of a function using the fixed point iteration method.

    Parameters:
    g (function): The iteration function g(x).
    x0 (float): Initial guess for the root.
    tolerance (float): Convergence tolerance.
    max_iterations (int): Maximum number of iterations.

    Returns:
    float: The approximate root.
    int: The number of iterations performed.
    """
    x = x0
    with open("fixed_point_iteration_output.txt", "w") as file:
        for i in range(max_iterations):

            # Open file to write output to
            x_next = g(x)

            # Write the output for each iteration
            file.write(f"x({i}) = {round(x_next, 5)}\n")
        
            print(f"Root(x{i}): {round(x_next, 5)} (found in {i} iterations)")
            if abs(x_next - x) < tolerance:

                # Write final output to file
                file.write(f"\nConverged to root: {round(x_next, 6)} in {i} iterations.\n")
                return f"Root: {round(x_next, 5)} (found in {i} iterations)"
            x = x_next
        raise ValueError("Fixed point iteration did not converge within the maximum number of iterations.")


def g(x):
    return math.sqrt(3 * x - 1)


result = fixed_point_iteration(g, 2.5, tolerance=1 * 10**-7)
print(result)