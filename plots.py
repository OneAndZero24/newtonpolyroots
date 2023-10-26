from typing import List, Tuple
import warnings

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import cplot

from newtonpolyroots import Polynomial


def stepsplot2d(domain: Tuple[float, float], p: Polynomial, steps: List[Tuple[float, float]]):
    start, stop = domain
    X = np.linspace(start, stop, 1000)
    y = [p(x) for x in X]
    plt.plot(X, y)
    plt.plot(X, np.zeros(len(X)), color='gray')
    h = list(map(list, zip(*steps[:-1])))
    plt.scatter(h[0], h[1], s=10, color='lime')
    plt.scatter(steps[-1][0], steps[-1][1], s=12, color='red', marker='x')
    plt.show()


def stepsplot3d(domain: Tuple[complex, complex], p: Polynomial, steps: List[Tuple[complex, complex]]):
    start, stop = domain
    _, ax = plt.subplots()
    cplt = cplot.plot(p, 
        (start.real, stop.real, 1000), 
        (start.imag, stop.imag, 1000),
    )
    X = steps[:-1][0]
    real = [x.real for x in X]
    imag = [x.imag for x in X]
    ax.scatter(real, imag, s=10, color='lime')
    ax.scatter(steps[-1][0].real, steps[-1][0].imag, s=12, color='red', marker='x')
    cplt.show()


def rootsplot(domain: Tuple[complex, complex], roots: List[complex], Y: List[List[int]], R: int):
    start, stop = domain
    rreal = [((x.real-start.real)/(stop.real-start.real))*R for x in roots]
    rimag = [((x.imag+stop.real)/(stop.imag-start.imag))*R for x in roots]
    plt.axis('off')
    plt.imshow(Y, cmap='hsv', origin='lower')
    plt.scatter(rreal, rimag, s=12, color='black', marker='x')
    plt.show()