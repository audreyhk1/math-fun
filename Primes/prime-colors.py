import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

def main():
    # create an array with all colors
    color_array = create_color_array()
    
    # get all primes
    primes_array = get_primes()
    

# create an array with all colors RGB as tuples
def create_color_array():
    color_array = []
    for a in range(0, 255):
        for b in range(0, 255):
            for c in range(0, 255):
                color_array.append((a, b, c))
    return color_array

# retrieve all primes from 2 to N
# courtesy of https://stackoverflow.com/questions/11619942/print-series-of-prime-numbers-in-python
def get_primes(end_prime = N_PRIMES):
    primes = [2]
    for num in range(3,end_prime,2):
        if all(num % i != 0 for i in range(2,int(math.sqrt(num))+1)):
            # add to an array
            primes.append(num)
    
    return primes

if __name__ == "__main__":
    main()