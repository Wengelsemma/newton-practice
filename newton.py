def first_der(f, x, eps=1e-5):
    return (f(x + eps) - f(x)) / eps
    """Optimization is an iterative algorithm used to find minimum of a function.
    where maxiter is the maximum number of iteration and eps is epsilion to measure closeness to x 
    """


def second_der(f, x, eps=1e-5):
    return (f(x + eps) - 2 * f(x) + f(x - eps)) / (eps**2)


def optimize(start, f, maxiter=100, tol=1e-6, eps=1e-6):
    x = float(start)
    for i in range(maxiter):
        g = first_der(f, x, eps)
        h = second_der(f, x, eps)
    if abs(g) < tol:
        return x
    if h == 0:
        return x
    xnew = x - (g / h)
    x = xnew
    return x
