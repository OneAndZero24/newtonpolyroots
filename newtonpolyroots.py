# Jan Miksa

from typing import List, Tuple, Set

import numpy as np

from progress.bar import Bar


class Polynomial():
    """
    Polynomial class constructed around list of coefficients from smallest degree
    """

    def __init__(self, coefs: List[float]):
        if not len(coefs):
            raise Exception("Polynomial coefficients cannot be empty!")
        alpha = 1
        j = 0
        for i, e in enumerate(coefs):
            if e != 0.0:
                j = i
                if abs(e) < alpha:
                    alpha = e

        coefs = [x/alpha if abs(x) > 0 else 0 for x in coefs]

        self.coefs = coefs[:(j+1)]
        self.deg = len(self.coefs)-1

    def __str__(self) -> str:
        r = str(self.coefs[0])
        for i, c in enumerate(self.coefs[1:], 1):
            r += ("+"+str(c)+"x^"+str(i))
        return r

    def __call__(self, x: complex) -> complex:
        # Horner's method
        r = self.coefs[-1]
        for c in reversed(self.coefs[:-1]):
            r *= x
            r += c
        return r
        

def polyderiv(p: Polynomial) -> Polynomial:
    """
    Calculates derivative of given polynomial, returns new instance
    """

    oldcoefs = p.coefs
    if len(oldcoefs) > 1:
        newcoefs = oldcoefs[1:]                 # Shift coefficients
        for i in range(1, len(oldcoefs), 1):    # Multiply by powers
            newcoefs[i-1] *= i
        return Polynomial(newcoefs)
    else:
        return 0.0
    

def newton(p: Polynomial, x: complex, E: float, G: float, I: int, d: Polynomial=None) -> List[Tuple[complex, complex]]:
    """
    Performs newton method descent until given epsilon `E` is achieved or iteration number reached\n
    Returns list of steps `[(step_x, step_y)]` - last one is result
    """

    if d is None:
        d = polyderiv(p)
    steps = []

    def _step(y: complex) -> Tuple[complex, complex]:
        # Util to append steps
        val = p(y)
        r = (y, val)
        steps.append(r)
        return r

    i = 0
    c_x, c_val = _step(x)
    old_x = c_x+2*G
    while (abs(c_val) > E) and (abs(old_x-c_x) > G) and i < I:
        old_x = c_x
        new_x = c_x-(c_val/d(c_x))  # Newton's method step
        c_x, c_val = _step(new_x)
        i += 1

    return steps


def roots(p: Polynomial, domain: Tuple[complex, complex], E: float, G: float, I: int, R: int) -> Tuple[List[complex], List[List[int]]]:
    """
    Finds all roots of given polynomial based on newtons method
    """

    start, stop = domain

    # Grid for sampling starting points
    realX = np.linspace(start.real, stop.real, R)
    imagX = np.linspace(start.real, stop.real, R)

    roots = []
    Y = np.ndarray(shape=(R, R))    # For roots markers - to color appropriate basins

    def _addroot(root: complex) -> int:
        # Checks if new root detected, returns its index
        for i, r in enumerate(roots):
            if abs(r-root) < G:
                return i+1
        roots.append(root)
        return len(roots)+1

    dp = polyderiv(p)

    # Starting newtons method at each grid point
    with Bar('Calculating', max=R*R) as bar:
        for i, x in enumerate(realX):
            for j, y in enumerate(imagX):
                step = newton(p, complex(x, y), E, G, I, dp)[-1]
                croot, cval = step
                key = 0
                if abs(cval) < E:
                    key = _addroot(croot)
                Y[i][j] = key
                bar.next()
    
    return (roots, Y.tolist())