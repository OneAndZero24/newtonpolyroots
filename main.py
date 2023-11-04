import sys
import warnings

from newtonpolyroots import *
from plots import *


warnings.filterwarnings("ignore")
                        
EPSILON = 10e-9
GAMMA = 10e-9
LIMIT = 10000
RESOLUTION = 1000


def main():
    print("Please provide polynomial coefficients in a single line, separated by single space, from lowest to highest degree.")
    print("Example for z^6+z^3-1:")
    print("-1 0 0 1 0 0 1")

    coefs = [float(x) for x in sys.stdin.readline().split(' ')]

    p = Polynomial(coefs)
    print("Recieved polynomial:")
    print(p)

    # Cauchy bound
    C = p.coefs[-1]
    R = 1+max([abs(x/C) for x in p.coefs[:-1]])

    domain = (complex(-R, -R), complex(R, R))

    r, Y = roots(p, domain, EPSILON, GAMMA, LIMIT, RESOLUTION)
    print(r)
    rootsplot(domain, r, Y, RESOLUTION)

if __name__ == "__main__":
    main()
