#multivariate newton
import numpy as np

from scipy.linalg import solve
def multinewton(x0, f, maxiter=100, e=1e-5):
    x=np.array(x0, datatype=float)
    for i in range(maxiter):
        g= first_der(f, x, eps)
        h=second_der(f, x, eps)
    gradhess= solve(h, g)
    xnew= x-gradhess
    if np.linalg.norm (xnew-x) < tol:
        return xnew
    x=xnew 
    return x
        
