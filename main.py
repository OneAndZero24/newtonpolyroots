import sys
import warnings

from newtonpolyroots import *
from plots import *


warnings.filterwarnings("ignore")
                        
EPSILON = 10e-6
GAMMA = 10e-3
LIMIT = 10e3
RESOLUTION = 1000


def main():
    print("Please provide polynomial coefficients in a single line, separated by single space, from lowest to highest degree.")
    print("Example for z^6+z^3-1:")
    print("-1 0 0 1 0 0 1")

    coefs = [float(x) for x in sys.stdin.readline().split(' ')]

    p = Polynomial(coefs)
    print("Recieved polynomial:")
    print(p)

    r, Y = roots(p, (-2.0-2.0j,2.0+2.0j), EPSILON, GAMMA, LIMIT, RESOLUTION)
    print(r)
    rootsplot((-2.0-2.0j,2.0+2.0j), r, Y, RESOLUTION)

if __name__ == "__main__":
    main()
