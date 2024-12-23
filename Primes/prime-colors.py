import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

def main():
    # create an array with all colors
    color_array = create_color_array()
    
    # get all primes

def create_color_array():
    color_array = []
    for a in range(0, 255):
        for b in range(0, 255):
            for c in range(0, 255):
                color_array.append((a, b, c))
    return color_array


if __name__ == "__main__":
    main()