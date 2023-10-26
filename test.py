import warnings

from newtonpolyroots import *
from plots import *


warnings.filterwarnings("ignore")
                        
EPSILON = 10e-6
GAMMA = 10e-3
LIMIT = 10e3
RESOLUTION = 1000


def main():
    # 3x^6+2x^3+1
    coefs = [1, 0, 0, 2, 0, 0, 3]

    print('---Polynomial output test---')
    p = Polynomial(coefs)
    print(p)

    print('---Henon test---')
    print(p(1.0+1.0j))

    print('---Derivate test---')
    print(polyderiv(p))

    print('---Newton test---')
    steps = newton(p, 1.0+1.0j, EPSILON, LIMIT)
    print(steps)
    realsteps = [(x.real, y.real) for x, y in steps]
    stepsplot2d((-1.0, 1.0), p, realsteps)
    stepsplot3d((-2.0-2.0j,2.0+2.0j), p, steps)

    print('---Roots test---')
    r, Y = roots(p, (-2.0-2.0j,2.0+2.0j), EPSILON, GAMMA, LIMIT, RESOLUTION)
    print(r)
    rootsplot((-2.0-2.0j,2.0+2.0j), r, Y, RESOLUTION)

if __name__ == "__main__":
    main()
